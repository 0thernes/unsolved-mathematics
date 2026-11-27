<#
.SYNOPSIS
    Windows build automation for The Unsolved Mathematics Atlas (bracket-safe).
.DESCRIPTION
    PowerShell equivalent of justfile / Makefile. Run a target, e.g.:
        ./build.ps1 all
        ./build.ps1 check
        ./build.ps1 query -Q "connection between RH and random matrices"
.PARAMETER Target
    One of: build, check, validate, corpus, index, papers, register, site, embed, query, formal, lint, mutate, audit, test, all, clean, help
#>
[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [ValidateSet('build', 'check', 'validate', 'corpus', 'index', 'papers', 'register', 'site', 'embed', 'query', 'formal', 'lint', 'mutate', 'audit', 'test', 'all', 'clean', 'help')]
    [string]$Target = 'help',

    [string]$Q = ''
)

$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true
$py = if ($env:PY) { $env:PY } else { 'python' }
$root = $PSScriptRoot

function Invoke-Step($desc, [scriptblock]$block) {
    Write-Host "==> $desc" -ForegroundColor Cyan
    & $block
}

function Invoke-AllChecks {
    & $py "$root/scripts/generate.py" --check
    & $py "$root/scripts/validate.py"
    & $py "$root/scripts/check_dossiers.py" --strict
    & $py "$root/scripts/check_papers.py"
    & $py "$root/scripts/proof_claim_sweep.py"
    & $py "$root/scripts/check_retractions.py" --check
    & $py "$root/scripts/check_readme_axioms.py"
    & $py "$root/scripts/sync_external_programs.py" --check
    & $py "$root/scripts/build_data_manifest.py" --check
    & $py "$root/scripts/timestamp_manifest.py" --check
}

switch ($Target) {
    'build'    { Invoke-Step 'Regenerate atlas'          { & $py "$root/scripts/generate.py" } }
    'check'    { Invoke-Step 'Full integrity gate'       { Invoke-AllChecks } }
    'validate' { Invoke-Step 'Full integrity gate'       { Invoke-AllChecks } }
    'corpus'   { Invoke-Step 'Build RAG corpus'          { & $py "$root/rag/build_corpus.py" } }
    'index'    { Invoke-Step 'Build cross-indexes'       { & $py "$root/scripts/build_indexes.py" } }
    'papers'   { Invoke-Step 'Meta-analysis integrity'   { & $py "$root/scripts/check_papers.py" } }
    'register' { Invoke-Step 'Build review register'     { & $py "$root/scripts/build_review_register.py" } }
    'site'     { Invoke-Step 'Build static site + DAG'   { & $py "$root/scripts/build_site.py" } }
    'embed'    { Invoke-Step 'Build dense index'         { & $py "$root/rag/embed_index.py" } }
    'query'    { Invoke-Step "Query: $Q"                 { & $py "$root/rag/retriever.py" $Q } }
    'formal'   {
        Invoke-Step 'Build & verify Lean 4.35.0 formal core' {
            Push-Location -LiteralPath "$root/lean"
            try {
                lake build Challenge Solution NonVacuity Adversarial
                lake env lean VerifyAxioms.lean
                lake env leanchecker-paranoid --fresh Solution
                lake env leanchecker-paranoid --fresh NonVacuity
                lake env leanchecker-paranoid --fresh Adversarial
            } finally {
                Pop-Location
            }
            & $py "$root/scripts/test_lean_negative.py"
        }
    }
    'lint'     {
        Invoke-Step 'Report-only ruff & mypy' {
            ruff check "$root/scripts" "$root/rag" "$root/tests" "$root/examples"
            ruff check --select E9,F63,F7,F82,B023 "$root/problems/collatz-conjecture/experiments"
            mypy --explicit-package-bases "$root/scripts" "$root/rag" "$root/examples"
        }
    }
    'mutate'   { Invoke-Step 'Run mutation suite'        { & $py "$root/tests/mutation_check.py" } }
    'audit'    { Invoke-Step 'Build Standard v1.2.0'     { pwsh -File "$root/scripts/Audit-Repo.ps1" -Path $root } }
    'test'     {
        Invoke-Step 'Run full verification test ladder' {
            & $py -m pytest -v "$root/tests"
            & $py "$root/tests/mutation_check.py"
        }
    }
    'all'      {
        Invoke-Step 'Regenerate atlas'          { & $py "$root/scripts/generate.py" }
        Invoke-Step 'Build RAG corpus'          { & $py "$root/rag/build_corpus.py" }
        Invoke-Step 'Build cross-indexes'       { & $py "$root/scripts/build_indexes.py" }
        Invoke-Step 'Build review register'     { & $py "$root/scripts/build_review_register.py" }
        Invoke-Step 'Build static site + DAG'   { & $py "$root/scripts/build_site.py" }
        Invoke-Step 'Full integrity gate'       { Invoke-AllChecks }
        Invoke-Step 'Run full test ladder'      { & $py -m pytest -v "$root/tests"; & $py "$root/tests/mutation_check.py" }
    }
    'clean'    {
        Invoke-Step 'Clean artifacts (bracket-safe)' {
            $npz = Join-Path $root 'rag/index.npz'
            if (Test-Path -LiteralPath $npz) { Remove-Item -LiteralPath $npz -Force }
            Get-ChildItem -LiteralPath $root -Recurse -Directory -Filter '__pycache__' -ErrorAction SilentlyContinue |
                ForEach-Object { Remove-Item -LiteralPath $_.FullName -Recurse -Force -ErrorAction SilentlyContinue }
        }
    }
    default {
        Write-Host "Targets: build | check | corpus | index | papers | register | site | embed | query -Q '...' | formal | lint | mutate | audit | test | all | clean" -ForegroundColor Yellow
    }
}
