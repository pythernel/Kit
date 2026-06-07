# setup.ps1 — Install Kit as a global command
$kitDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$kitPy = Join-Path $kitDir "kit.py"

# Create a .bat wrapper in a directory that's in PATH
$wrapperDir = "$env:USERPROFILE\.kit-bin"
New-Item -ItemType Directory -Path $wrapperDir -Force | Out-Null

$batPath = Join-Path $wrapperDir "kit.bat"
@"
@echo off
python "$kitPy" %*
"@ | Set-Content -Path $batPath

# Add to PATH if not already
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($userPath -notlike "*$wrapperDir*") {
    [Environment]::SetEnvironmentVariable("Path", "$userPath;$wrapperDir", "User")
    $env:Path = [Environment]::GetEnvironmentVariable("Path", "User") + ";" + [Environment]::GetEnvironmentVariable("Path", "Machine")
}

Write-Host "[+] Kit installed. Restart your terminal, then use: kit <command>"
Write-Host "    Example: kit scan 127.0.0.1 -p 22,80,443"
