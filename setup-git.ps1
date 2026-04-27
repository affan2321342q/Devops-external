# Git Setup Script for Todo App
# This PowerShell script initializes Git repository and creates the workflow

$ErrorActionPreference = "Continue"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Todo App - Git Repository Setup Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Git is installed
Write-Host "[1/6] Checking Git installation..." -ForegroundColor Yellow

# Try Get-Command first (works if git is on PATH)
$gitCmd = Get-Command git -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source -ErrorAction SilentlyContinue

# Fallback to common install locations
if (-not $gitCmd) {
    $possible = @(
        "$env:LOCALAPPDATA\Programs\Git\cmd\git.exe",
        "$env:LOCALAPPDATA\Programs\Git\bin\git.exe",
        "C:\Program Files\Git\cmd\git.exe",
        "C:\Program Files (x86)\Git\cmd\git.exe",
        "$env:ProgramFiles\Git\cmd\git.exe",
        "$env:ProgramFiles(x86)\Git\cmd\git.exe",
        "$env:LOCALAPPDATA\Programs\Git\mingw64\bin\git.exe"
    )
    foreach ($p in $possible) {
        if (Test-Path $p) { $gitCmd = $p; break }
    }
}

if (-not $gitCmd) {
    Write-Host "Git is not installed!" -ForegroundColor Red
    Write-Host "Please install Git from: https://git-scm.com/download/win" -ForegroundColor Red
    exit 1
}

# Get version using the resolved git command
try {
    $gitVersion = & $gitCmd --version 2>$null
    Write-Host "Git found: $gitVersion" -ForegroundColor Green
}
catch {
    Write-Host "Git executable found but failed to run." -ForegroundColor Red
    Write-Host "Please check your Git installation." -ForegroundColor Red
    exit 1
}

# Configure Git user
Write-Host "[2/6] Configuring Git user..." -ForegroundColor Yellow
git config --global user.email "test@example.com"
git config --global user.name "Test User"
Write-Host "Git user configured" -ForegroundColor Green

# Initialize repository
Write-Host "[3/6] Initializing Git repository..." -ForegroundColor Yellow
if (Test-Path ".git") {
    Write-Host "Git repository already initialized" -ForegroundColor Green
}
else {
    git init
    Write-Host "Git repository initialized" -ForegroundColor Green
}

# Add files and initial commit
Write-Host "[4/6] Creating initial commit..." -ForegroundColor Yellow
git add .
git commit -m "Initial commit: Todo app setup with HTML, CSS, JS, Docker, and Selenium tests"
Write-Host "Initial commit created" -ForegroundColor Green

# Create feature branch
Write-Host "[5/6] Creating and merging feature branch..." -ForegroundColor Yellow
git checkout -b feature/add-categories
Add-Content -Path "CHANGELOG.md" -Value "`nUpdated with new category features"
git add CHANGELOG.md
git commit -m "Add categories feature to changelog - Feature branch commit"
git checkout main
git merge feature/add-categories --no-edit
Write-Host "Feature branch created and merged" -ForegroundColor Green

# Display git history
Write-Host "[6/6] Displaying commit history..." -ForegroundColor Yellow
Write-Host ""
git log --oneline --graph
Write-Host ""

# Display branch info
Write-Host "Branch Information:" -ForegroundColor Cyan
git branch -a
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host "1. Create repository on GitHub" -ForegroundColor White
Write-Host "2. Add remote: git remote add origin https://github.com/affan2321342q/todo-app.git" -ForegroundColor White
Write-Host "3. Push code: git push -u origin main" -ForegroundColor White
Write-Host "4. Push branches: git push -u origin --all" -ForegroundColor White
Write-Host ""
