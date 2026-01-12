@echo off
echo Starting Jarvis Voice Assistant...
echo.

REM Check if virtual environment exists and activate it
if exist venv\Scripts\activate.bat (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
)

REM Check if .env file exists
if not exist .env (
    echo ERROR: .env file not found!
    echo Please run setup.bat first or create .env file manually
    echo.
    pause
    exit /b 1
)

REM Run Jarvis
python Jarvis.py

pause
