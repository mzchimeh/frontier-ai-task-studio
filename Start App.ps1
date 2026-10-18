$ErrorActionPreference = 'Stop'
$taskAuthorPython = 'C:\Users\vared\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$taskAuthorScript = Join-Path $PSScriptRoot 'validation_server.py'
if (-not (Test-Path -LiteralPath $taskAuthorPython)) { throw 'The bundled Python runtime is unavailable. See README for startup instructions.' }
$taskAuthorRunning = $false
try {
    $taskAuthorResponse = Invoke-RestMethod -Uri 'http://127.0.0.1:8765/api/status' -TimeoutSec 2
    $taskAuthorRunning = [bool]$taskAuthorResponse.token
} catch { }
if (-not $taskAuthorRunning) {
    Start-Process -FilePath $taskAuthorPython -ArgumentList @(('"' + $taskAuthorScript + '"')) -WorkingDirectory $PSScriptRoot -WindowStyle Hidden
}
Start-Process 'http://127.0.0.1:8765/dist/validation.html'
