from __future__ import annotations

import argparse
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def slide_number(path: Path) -> int:
    match = re.search(r"(\d+)", path.stem)
    return int(match.group(1)) if match else 0


def label_font() -> ImageFont.ImageFont:
    for font_path in (
        "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ):
        try:
            return ImageFont.truetype(font_path, 18)
        except OSError:
            continue
    return ImageFont.load_default()


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a contact sheet from exported slide PNGs.")
    parser.add_argument("--input", required=True, help="Directory containing slide PNG files")
    parser.add_argument("--output", required=True, help="Output contact sheet PNG")
    parser.add_argument("--cols", type=int, default=3)
    parser.add_argument("--thumb-width", type=int, default=400)
    parser.add_argument("--thumb-height", type=int, default=225)
    args = parser.parse_args()

    source = Path(args.input).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    files = sorted(source.glob("*.png"), key=slide_number)
    if not files:
        raise SystemExit(f"No PNG files found in {source}")

    cols = max(1, args.cols)
    rows = (len(files) + cols - 1) // cols
    margin = 24
    label_h = 26
    tw, th = args.thumb_width, args.thumb_height
    sheet = Image.new("RGB", (cols * tw + (cols + 1) * margin, rows * (th + label_h) + (rows + 1) * margin), "white")
    draw = ImageDraw.Draw(sheet)
    font = label_font()

    for idx, path in enumerate(files):
        img = Image.open(path).convert("RGB").resize((tw, th), Image.Resampling.LANCZOS)
        col = idx % cols
        row = idx // cols
        x = margin + col * (tw + margin)
        y = margin + row * (th + label_h + margin)
        number = slide_number(path) or idx + 1
        draw.text((x, y), f"Slide {number}", fill=(0, 0, 0), font=font)
        sheet.paste(img, (x, y + label_h))

    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
