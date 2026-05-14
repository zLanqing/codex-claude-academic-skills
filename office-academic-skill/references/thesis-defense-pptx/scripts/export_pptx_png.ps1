param(
    [Parameter(Mandatory = $true)]
    [string]$Pptx,

    [Parameter(Mandatory = $true)]
    [string]$OutDir,

    [int]$Width = 1600,

    [int]$Height = 900
)

$ErrorActionPreference = "Stop"

# Windows console defaults to cp936/gbk; force UTF-8 so JSON with Chinese
# paths or special characters stays readable on stdout.
try {
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
    $OutputEncoding = [System.Text.Encoding]::UTF8
} catch {}

$pptxPath = [System.IO.Path]::GetFullPath($Pptx)
$outPath = [System.IO.Path]::GetFullPath($OutDir)

if (!(Test-Path -LiteralPath $pptxPath)) {
    throw "PPTX not found: $pptxPath"
}
New-Item -ItemType Directory -Force -Path $outPath | Out-Null
$existingPngs = Get-ChildItem -LiteralPath $outPath -Filter "*.PNG" -ErrorAction SilentlyContinue
if ($existingPngs.Count -gt 0) {
    throw "Output directory already contains PNG files. Use a fresh timestamped export directory: $outPath"
}

$pp = $null
$pres = $null
try {
    $pp = New-Object -ComObject PowerPoint.Application
    $pres = $pp.Presentations.Open($pptxPath, $true, $false, $false)
    $pres.Export($outPath, "PNG", $Width, $Height)
    $count = (Get-ChildItem -LiteralPath $outPath -Filter "*.PNG" | Measure-Object).Count
    [PSCustomObject]@{
        pptx = $pptxPath
        out_dir = $outPath
        slide_png_count = $count
    } | ConvertTo-Json -Compress
}
finally {
    if ($pres -ne $null) {
        try { $pres.Close() } catch {}
        [System.Runtime.InteropServices.Marshal]::ReleaseComObject($pres) | Out-Null
    }
    if ($pp -ne $null) {
        try { $pp.Quit() } catch {}
        [System.Runtime.InteropServices.Marshal]::ReleaseComObject($pp) | Out-Null
    }
}
