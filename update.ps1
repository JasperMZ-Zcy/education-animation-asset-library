[CmdletBinding()]
param(
    [switch]$NonInteractive
)

$ErrorActionPreference = 'Stop'

Push-Location $PSScriptRoot
try {
    git pull --ff-only
    if ($LASTEXITCODE -ne 0) {
        throw 'Git could not fast-forward the local checkout. Resolve local changes before updating.'
    }

    & (Join-Path $PSScriptRoot 'install.ps1') -NonInteractive:$NonInteractive
}
finally {
    Pop-Location
}
