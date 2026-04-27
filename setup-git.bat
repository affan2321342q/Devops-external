@echo off
REM Git Setup and Repository Initialization Script
REM This script initializes a Git repository and creates initial commits

echo.
echo ========================================
echo Todo App - Git Repository Setup
echo ========================================
echo.

REM Configure Git
echo [1/5] Configuring Git user...
git config --global user.email "test@example.com"
git config --global user.name "Test User"

REM Initialize repository
echo [2/5] Initializing Git repository...
git init

REM Add all files
echo [3/5] Adding files to staging area...
git add .

REM Make initial commit
echo [4/5] Creating initial commit...
git commit -m "Initial commit: Todo app with HTML, CSS, JS, Docker, and tests"

REM Create a feature branch
echo [5/5] Creating feature branch...
git checkout -b feature/add-categories

REM Create a sample change
echo Updated app with categories feature >> CHANGELOG.md
git add CHANGELOG.md
git commit -m "Add categories feature to changelog"

REM Merge back to main
git checkout main
git merge feature/add-categories --no-edit

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Git repository initialized successfully
echo Branch created and merged back to main
echo.
git log --oneline
echo.
echo Ready for GitHub upload!
echo.
pause
