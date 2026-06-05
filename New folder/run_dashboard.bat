@echo off
REM Habit Tracker Dashboard Launcher
REM This script activates the virtual environment and runs the Streamlit app

cd /d "%~dp0"
call .venv\Scripts\activate.bat
streamlit run dashboard/app.py
pause
