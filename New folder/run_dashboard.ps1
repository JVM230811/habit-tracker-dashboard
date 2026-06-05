# Habit Tracker Dashboard Launcher (PowerShell)
# This script activates the virtual environment and runs the Streamlit app

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

# Set execution policy for this session
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned -Force

# Activate virtual environment
& .\.venv\Scripts\Activate.ps1

# Run the dashboard
streamlit run dashboard/app.py
