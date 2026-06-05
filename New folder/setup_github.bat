@echo off
REM GitHub Setup Script for Habit Tracker Dashboard

echo.
echo ====================================
echo GitHub Repository Setup
echo ====================================
echo.

setlocal enabledelayedexpansion

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed!
    echo Download from: https://git-scm.com/download/win
    pause
    exit /b 1
)

REM Get GitHub username
set /p GITHUB_USER="Enter your GitHub username: "

if "!GITHUB_USER!"=="" (
    echo ERROR: GitHub username cannot be empty
    pause
    exit /b 1
)

echo.
echo Setting up GitHub repository...
echo Repository will be: https://github.com/!GITHUB_USER!/habit-tracker-dashboard
echo.

REM Initialize git
echo [1/6] Initializing git...
git init

REM Add all files
echo [2/6] Adding files...
git add .

REM Create commit
echo [3/6] Creating initial commit...
git commit -m "Initial commit: Habit Tracker Dashboard"

REM Rename branch to main
echo [4/6] Setting up main branch...
git branch -M main

REM Add remote
echo [5/6] Connecting to GitHub...
git remote add origin https://github.com/!GITHUB_USER!/habit-tracker-dashboard.git

REM Push to GitHub
echo [6/6] Pushing to GitHub...
echo Please sign in when prompted...
git push -u origin main

if errorlevel 1 (
    echo.
    echo ERROR: Failed to push to GitHub
    echo Make sure:
    echo 1. You created a repository at: https://github.com/!GITHUB_USER!/habit-tracker-dashboard
    echo 2. Your GitHub username is correct
    echo 3. You are signed into GitHub
    pause
    exit /b 1
)

echo.
echo ====================================
echo SUCCESS!
echo ====================================
echo.
echo Your project is now on GitHub!
echo Repository: https://github.com/!GITHUB_USER!/habit-tracker-dashboard
echo.
echo Next steps:
echo 1. Go to https://share.streamlit.io
echo 2. Click "Deploy an app"
echo 3. Enter:
echo    Repository: !GITHUB_USER!/habit-tracker-dashboard
echo    Branch: main
echo    Main file: dashboard/app.py
echo 4. Click "Deploy!"
echo.
pause
