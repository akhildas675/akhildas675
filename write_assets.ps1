$base = @'
iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAMAAWgmWQ0AAAAASUVORK5CYII=
'@
$data = [Convert]::FromBase64String($base)
$files = @('assets\bodometer.png','assets\soleway.png','assets\travel.png')
foreach ($f in $files) {
    $dir = Split-Path $f
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }
    [IO.File]::WriteAllBytes($f, $data)
}
Write-Host 'Written placeholders'