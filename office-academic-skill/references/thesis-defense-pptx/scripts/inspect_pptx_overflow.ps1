param(
    [Parameter(Mandatory = $true)]
    [string]$Pptx,

    [double]$Tolerance = 40,

    [string]$OutputJson = ""
)

$ErrorActionPreference = "Stop"

# Windows 默认 console 是 cp936/gbk，输出含中文路径或特殊符号的 JSON 会乱码。
# 强制切到 UTF-8 让 stdout 稳定可读；JSON 文件本身已用 UTF-8 写盘不受影响。
try {
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
    $OutputEncoding = [System.Text.Encoding]::UTF8
} catch {}

$pptxPath = [System.IO.Path]::GetFullPath($Pptx)
if (!(Test-Path -LiteralPath $pptxPath)) {
    throw "PPTX not found: $pptxPath"
}

$pp = $null
$pres = $null
$results = @()

function Test-ShapeOverflow {
    param(
        [Parameter(Mandatory = $true)]
        $Shape,

        [Parameter(Mandatory = $true)]
        [int]$SlideIndex,

        [string]$NamePrefix = ""
    )

    try {
        if ($Shape.Type -eq 6) {
            for ($i = 1; $i -le $Shape.GroupItems.Count; $i++) {
                Test-ShapeOverflow -Shape $Shape.GroupItems.Item($i) -SlideIndex $SlideIndex -NamePrefix "$NamePrefix$($Shape.Name)/"
            }
            return
        }
    }
    catch {
        # Non-standard shapes may not expose Type or GroupItems consistently.
    }

    try {
        if ($Shape.HasTextFrame -and $Shape.TextFrame.HasText) {
            $txt = $Shape.TextFrame.TextRange.Text.Trim()
            if ($txt.Length -gt 0) {
                $bw = $Shape.TextFrame2.TextRange.BoundWidth
                $bh = $Shape.TextFrame2.TextRange.BoundHeight
                $isOverflow = ($bw -gt ($Shape.Width + $Tolerance)) -or ($bh -gt ($Shape.Height + $Tolerance))
                if ($isOverflow) {
                    $short = $txt
                    if ($short.Length -gt 180) {
                        $short = $short.Substring(0, 180)
                    }
                    $short = $short -replace "`r|`n", " / "
                    $script:results += [PSCustomObject]@{
                        slide = $SlideIndex
                        shape = "$NamePrefix$($Shape.Name)"
                        width = [math]::Round($Shape.Width, 1)
                        bound_width = [math]::Round($bw, 1)
                        height = [math]::Round($Shape.Height, 1)
                        bound_height = [math]::Round($bh, 1)
                        text = $short
                    }
                }
            }
        }
    }
    catch {
        # Some shapes expose partial text APIs; skip them.
    }
}

try {
    $pp = New-Object -ComObject PowerPoint.Application
    $pres = $pp.Presentations.Open($pptxPath, $true, $false, $false)

    foreach ($slide in $pres.Slides) {
        try {
            $shapeCount = $slide.Shapes.Count
        }
        catch {
            continue
        }
        for ($i = 1; $i -le $shapeCount; $i++) {
            try {
                $shape = $slide.Shapes.Item($i)
                Test-ShapeOverflow -Shape $shape -SlideIndex $slide.SlideIndex
            }
            catch {
                # Skip shapes that fail COM enumeration.
            }
        }
    }
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

$payload = [PSCustomObject]@{
    pptx = $pptxPath
    tolerance = $Tolerance
    overflow_count = $results.Count
    overflows = $results
}

$json = $payload | ConvertTo-Json -Depth 6
if (![string]::IsNullOrWhiteSpace($OutputJson)) {
    $jsonPath = [System.IO.Path]::GetFullPath($OutputJson)
    $jsonDir = Split-Path -Parent $jsonPath
    if ($jsonDir -and !(Test-Path -LiteralPath $jsonDir)) {
        New-Item -ItemType Directory -Force -Path $jsonDir | Out-Null
    }
    Set-Content -LiteralPath $jsonPath -Value $json -Encoding UTF8
}
$json
