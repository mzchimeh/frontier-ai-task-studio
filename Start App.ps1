param(
    [string]$PythonPath,
    [switch]$NoBrowser,
    [switch]$Check
)
$ErrorActionPreference = 'Stop'
$taskAuthorScript = Join-Path $PSScriptRoot 'validation_server.py'
if (-not (Test-Path -LiteralPath $taskAuthorScript)) { throw 'validation_server.py is missing. Extract the complete application folder first.' }
$taskAuthorCandidates = @()
if ($PythonPath) {
    $taskAuthorCandidates += @{ File = $PythonPath; Args = @() }
} else {
    foreach ($taskAuthorName in @('py', 'python', 'python3')) {
        $taskAuthorCommand = Get-Command $taskAuthorName -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($taskAuthorCommand) {
            # Do not launch the Windows Store's python placeholder.
            if ($taskAuthorName -ne 'py' -and $taskAuthorCommand.Source -like '*\Microsoft\WindowsApps\*') { continue }
            $taskAuthorCandidates += @{ File = $taskAuthorCommand.Source; Args = $(if ($taskAuthorName -eq 'py') { @('-3') } else { @() }) }
        }
    }
}
$taskAuthorPython = $null
foreach ($taskAuthorCandidate in $taskAuthorCandidates) {
    try {
        $taskAuthorPrefix = $taskAuthorCandidate.Args
        $taskAuthorResult = & $taskAuthorCandidate.File @taskAuthorPrefix -c 'import sys; assert sys.version_info >= (3,11); print(sys.executable)' 2>$null
        if ($LASTEXITCODE -eq 0 -and $taskAuthorResult) {
            $taskAuthorResolved = ([string]($taskAuthorResult | Select-Object -Last 1)).Trim()
            if (Test-Path -LiteralPath $taskAuthorResolved -PathType Leaf) { $taskAuthorPython = $taskAuthorResolved; break }
        }
    } catch { }
}
if (-not $taskAuthorPython) { throw 'Python 3.11 or newer was not found. Install Python, reopen PowerShell, or use .\Start App.ps1 -PythonPath "C:\path\to\python.exe". See README.md.' }
if ($Check) { Write-Output ('Python ready: ' + $taskAuthorPython); exit 0 }
$taskAuthorPort = 8765
if ($env:TASK_AUTHOR_PORT) {
    if (-not [int]::TryParse($env:TASK_AUTHOR_PORT, [ref]$taskAuthorPort) -or $taskAuthorPort -lt 1024 -or $taskAuthorPort -gt 65535) { throw 'TASK_AUTHOR_PORT must be an integer from 1024 to 65535.' }
}
$taskAuthorOrigin = 'http://127.0.0.1:' + $taskAuthorPort
$taskAuthorExpectedRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot 'workspace\tasks')).TrimEnd('\','/')
function Get-TaskAuthorServer {
    try { return Invoke-RestMethod -Uri ($taskAuthorOrigin + '/api/status') -TimeoutSec 10 } catch { return $null }
}
$taskAuthorResponse = Get-TaskAuthorServer
if ($taskAuthorResponse -and (-not $taskAuthorResponse.token -or $taskAuthorResponse.taskRoot.TrimEnd('\','/') -ne $taskAuthorExpectedRoot)) {
    throw ('Port ' + $taskAuthorPort + ' is already used by a different app folder. Close that runner or choose a different TASK_AUTHOR_PORT.')
}
if (-not $taskAuthorResponse) {
    $taskAuthorLogs = Join-Path $PSScriptRoot 'runtime'
    New-Item -ItemType Directory -Path $taskAuthorLogs -Force | Out-Null
    $taskAuthorProcess = Start-Process -FilePath $taskAuthorPython -ArgumentList @(('"' + $taskAuthorScript + '"')) -WorkingDirectory $PSScriptRoot -WindowStyle Hidden -RedirectStandardOutput (Join-Path $taskAuthorLogs 'startup.log') -RedirectStandardError (Join-Path $taskAuthorLogs 'startup-error.log') -PassThru
    for ($taskAuthorAttempt = 0; $taskAuthorAttempt -lt 40; $taskAuthorAttempt++) {
        Start-Sleep -Milliseconds 250
        $taskAuthorResponse = Get-TaskAuthorServer
        if ($taskAuthorResponse) { break }
        if ($taskAuthorProcess.HasExited) { break }
    }
}
if (-not $taskAuthorResponse -or -not $taskAuthorResponse.token -or $taskAuthorResponse.taskRoot.TrimEnd('\','/') -ne $taskAuthorExpectedRoot) { throw 'The local runner did not start for this folder. Check runtime/startup-error.log and ensure the port is free.' }
Write-Output ('App ready: ' + $taskAuthorOrigin + '/dist/validation.html')
if (-not $NoBrowser) { Start-Process ($taskAuthorOrigin + '/dist/validation.html') }
