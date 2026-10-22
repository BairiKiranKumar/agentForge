# Headless Chrome screenshots at three widths.
# Usage: powershell -File shoot.ps1 <html-path> <outdir> <label>
# Headless Chrome will not lay out below about 500 px wide, so 375 px is captured by
# loading the page in a 375 px wide iframe inside a wrapper page. The PNG is wider than
# 375 px (white margin on the right); the page itself is laid out at 375 CSS px.
param($Html, $OutDir, $Label)
$chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
New-Item -ItemType Directory -Force $OutDir | Out-Null
$full = (Resolve-Path $Html).Path
$url = "file:///" + $full.Replace('\', '/')
$outDirFull = (Resolve-Path $OutDir).Path
foreach ($w in 768, 1440) {
  $out = Join-Path $outDirFull "$Label-$w.png"
  & $chrome --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=3000 "--window-size=$w,900" "--screenshot=$out" $url 2>$null | Out-Null
}
$wrap = Join-Path $outDirFull "$Label-375-wrapper.html"
"<!doctype html><body style='margin:0;background:#ccc'><iframe src='$url' width='375' height='800' style='border:0;background:#fff'></iframe></body>" | Set-Content -Encoding utf8 $wrap
$wurl = "file:///" + $wrap.Replace('\', '/')
& $chrome --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=3000 "--window-size=520,800" "--screenshot=$(Join-Path $outDirFull "$Label-375.png")" $wurl 2>$null | Out-Null
Remove-Item $wrap -ErrorAction SilentlyContinue
