from __future__ import annotations

import argparse
import re
from pathlib import Path


TEXT_EXTS = {".tex", ".bib", ".md", ".txt"}
FIG_EXTS = {".png", ".jpg", ".jpeg", ".svg", ".pdf"}
FIG_DIR_HINTS = ("figure", "fig", "image", "img", "图", "插图")


def read_pdf(path: Path, max_pages: int | None = None) -> str:
    try:
        import pymupdf as fitz
    except Exception:
        try:
            import fitz  # PyMuPDF legacy import
        except Exception:
            fitz = None

    if fitz is not None:
        parts: list[str] = []
        doc = fitz.open(path)
        try:
            limit = min(len(doc), max_pages or len(doc))
            for i in range(limit):
                parts.append(doc[i].get_text("text"))
        finally:
            doc.close()
        return "\n".join(parts)

    try:
        from pypdf import PdfReader
    except Exception as exc:
        raise RuntimeError("Install PyMuPDF or pypdf to extract PDF text") from exc

    reader = PdfReader(str(path))
    pages = reader.pages[: max_pages or len(reader.pages)]
    return "\n".join(page.extract_text() or "" for page in pages)


def clean_text(text: str) -> str:
    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_tex_sections(text: str) -> list[tuple[str, str]]:
    pattern = re.compile(r"\\(?:chapter|section|subsection)\*?\{([^}]+)\}")
    matches = list(pattern.finditer(text))
    sections: list[tuple[str, str]] = []
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        sections.append((match.group(1).strip(), clean_text(body)[:1600]))
    return sections


def read_text_with_fallback(path: Path) -> str | None:
    for enc in ("utf-8", "gb18030", "gbk", "utf-8-sig"):
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            continue
        except OSError:
            return None
    return None


def collect_files(root: Path) -> tuple[list[Path], list[Path], list[Path]]:
    if root.is_file():
        files = [root]
    else:
        files = [p for p in root.rglob("*") if p.is_file()]

    pdfs = [p for p in files if p.suffix.lower() == ".pdf"]
    texts = [p for p in files if p.suffix.lower() in TEXT_EXTS]
    figs = [
        p
        for p in files
        if p.suffix.lower() in FIG_EXTS and any(h in str(p.parent).lower() for h in FIG_DIR_HINTS)
    ]
    if not figs:
        figs = [p for p in files if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".svg"}]
    return pdfs, texts, figs


def pick_main_pdf(pdfs: list[Path]) -> Path | None:
    if not pdfs:
        return None
    names = ("thesis", "main", "paper", "论文", "毕业")
    scored = []
    for p in pdfs:
        score = sum(1 for n in names if n.lower() in p.name.lower())
        score += p.stat().st_size / 1_000_000
        scored.append((score, p))
    return sorted(scored, reverse=True)[0][1]


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract thesis context from a PDF/LaTeX project.")
    parser.add_argument("--input", required=True, help="Thesis PDF, source file, or project directory")
    parser.add_argument("--output", required=True, help="Markdown output path")
    parser.add_argument("--max-pages", type=int, default=80, help="Maximum PDF pages to extract")
    args = parser.parse_args()

    root = Path(args.input).expanduser().resolve()
    out = Path(args.output).expanduser().resolve()
    pdfs, text_files, figures = collect_files(root)

    lines: list[str] = []
    lines.append("# Thesis Context Extract")
    lines.append("")
    lines.append(f"- Input: `{root}`")
    lines.append(f"- PDF files: {len(pdfs)}")
    lines.append(f"- Text/TeX files: {len(text_files)}")
    lines.append(f"- Candidate figures: {len(figures)}")
    lines.append("")

    main_pdf = pick_main_pdf(pdfs)
    if main_pdf:
        lines.append("## Main PDF Text")
        lines.append(f"Source: `{main_pdf}`")
        lines.append("")
        try:
            lines.append(clean_text(read_pdf(main_pdf, args.max_pages))[:30000])
        except Exception as exc:
            lines.append(f"PDF extraction failed: {exc}")
        lines.append("")

    tex_files = [p for p in text_files if p.suffix.lower() == ".tex"]
    if tex_files:
        lines.append("## LaTeX Sections")
        for tex in sorted(tex_files)[:20]:
            text = read_text_with_fallback(tex)
            if text is None:
                continue
            sections = extract_tex_sections(text)
            if not sections:
                continue
            lines.append(f"### `{tex.relative_to(root) if root.is_dir() else tex.name}`")
            for title, body in sections[:12]:
                lines.append(f"#### {title}")
                lines.append(body)
                lines.append("")

    if figures:
        lines.append("## Candidate Figures")
        for fig in sorted(figures)[:80]:
            try:
                rel = fig.relative_to(root) if root.is_dir() else fig.name
            except ValueError:
                rel = fig
            lines.append(f"- `{rel}`")

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
