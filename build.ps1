<#
.SYNOPSIS
    Windows build automation for The Unsolved Mathematics Atlas.
.DESCRIPTION
    PowerShell equivalent of the Makefile. Run a target, e.g.:
        ./build.ps1 all
        ./build.ps1 query -Q "connection between RH and random matrices"
.PARAMETER Target
    One of: build, check, corpus, index, embed, query, test, all, clean, help
#>
[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [ValidateSet('build', 'check', 'validate', 'corpus', 'index', 'embed', 'query', 'test', 'all', 'clean', 'help')]
    [string]$Target = 'help',

    [string]$Q = ''
)

$ErrorActionPreference = 'Stop'
$py = if ($env:PY) { $env:PY } else { 'python' }
$root = $PSScriptRoot

function Invoke-Step($desc, [scriptblock]$block) {
    Write-Host "==> $desc" -ForegroundColor Cyan
    & $block
}

switch ($Target) {
    'build'    { Invoke-Step 'Regenerate atlas'        { & $py "$root/scripts/generate.py" } }
    'check'    { Invoke-Step 'Validate'                { & $py "$root/scripts/generate.py" --check; & $py "$root/scripts/validate.py" } }
    'validate' { Invoke-Step 'Validate'                { & $py "$root/scripts/generate.py" --check; & $py "$root/scripts/validate.py" } }
    'corpus'   { Invoke-Step 'Build RAG corpus'        { & $py "$root/rag/build_corpus.py" } }
    'index'    { Invoke-Step 'Build cross-indexes'     { & $py "$root/scripts/build_indexes.py" } }
    'embed'    { Invoke-Step 'Build dense index'       { & $py "$root/rag/embed_index.py" } }
    'query'    { Invoke-Step "Query: $Q"               { & $py "$root/rag/retriever.py" $Q } }
    'test'     { Invoke-Step 'Run tests'              { & $py "$root/tests/test_atlas.py" } }
    'all'      {
        Invoke-Step 'Regenerate atlas' { & $py "$root/scripts/generate.py" }
        Invoke-Step 'Build RAG corpus' { & $py "$root/rag/build_corpus.py" }
        Invoke-Step 'Build cross-indexes' { & $py "$root/scripts/build_indexes.py" }
        Invoke-Step 'Validate' { & $py "$root/scripts/generate.py" --check; & $py "$root/scripts/validate.py" }
        Invoke-Step 'Run tests' { & $py "$root/tests/test_atlas.py" }
    }
    'clean'    {
        Invoke-Step 'Clean artifacts' {
            Remove-Item "$root/rag/index.npz" -ErrorAction SilentlyContinue
            Get-ChildItem $root -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
        }
    }
    default {
        Write-Host "Targets: build | check | corpus | index | embed | query -Q '...' | test | all | clean" -ForegroundColor Yellow
    }
}
