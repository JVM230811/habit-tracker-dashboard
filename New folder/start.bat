@echo off
REM ========================================
REM Habit Tracker Dashboard - Setup & Run
REM ========================================
REM This script handles first-time setup and launches the dashboard

cd /d "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

REM Check if virtual environment exists, if not create it
if not exist ".venv\" (
    echo.
    echo Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
)

REM Activate virtual environment
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

REM Check if requirements are installed
python -c "import streamlit; import pandas; import plotly" >nul 2>&1
if errorlevel 1 (
    echo.
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
)

REM Launch the dashboard
echo.
echo ========================================
echo Launching Habit Tracker Dashboard...
echo ========================================
echo.
echo Dashboard will open at: http://localhost:8501
echo Press Ctrl+C to stop the server
echo.

streamlit run dashboard/app.py --logger.level=error
