[CmdletBinding()]
param(
    [switch]$NonInteractive
)

$ErrorActionPreference = 'Stop'

$source = Join-Path $PSScriptRoot 'skill\education-animation-asset-library'
$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
$targetRoot = Join-Path $codexHome 'skills'
$target = Join-Path $targetRoot 'education-animation-asset-library'

if (-not (Test-Path -LiteralPath $source)) {
    throw "Skill source is missing: $source"
}

New-Item -ItemType Directory -Path $targetRoot -Force | Out-Null

if (Test-Path -LiteralPath $target) {
    $stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
    $backupRoot = Join-Path $codexHome 'skill-backups'
    $backup = Join-Path $backupRoot "education-animation-asset-library-$stamp"
    New-Item -ItemType Directory -Path $backupRoot -Force | Out-Null
    Copy-Item -LiteralPath $target -Destination $backup -Recurse -Force
    Remove-Item -LiteralPath $target -Recurse -Force
    Write-Host "Existing skill backed up to $backup"
}

Copy-Item -LiteralPath $source -Destination $target -Recurse -Force
Write-Host "Installed education-animation-asset-library to $target"
Write-Host 'Restart Codex or open a new task to load the Skill.'
