@echo off
echo ========================================
echo Jarvis Voice Assistant - Setup Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Python found!
python --version
echo.

REM Create virtual environment (optional but recommended)
echo [2/4] Do you want to create a virtual environment? (Recommended)
set /p create_venv="Enter Y for Yes, N for No: "
if /i "%create_venv%"=="Y" (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Virtual environment created and activated!
) else (
    echo Skipping virtual environment creation...
)
echo.

REM Install dependencies
echo [3/4] Installing dependencies...
echo.

REM Try to install PyAudio using pipwin first
echo Installing pipwin for easier PyAudio installation...
pip install pipwin
echo.

echo Installing PyAudio...
pipwin install pyaudio
if errorlevel 1 (
    echo Warning: pipwin failed, trying direct pip install...
    pip install PyAudio
    if errorlevel 1 (
        echo.
        echo WARNING: PyAudio installation failed!
        echo You may need to install it manually.
        echo See README.md for instructions.
        echo.
    )
)

echo Installing other dependencies...
pip install SpeechRecognition pyttsx3 requests python-dotenv
echo.

REM Setup .env file
echo [4/4] Setting up environment file...
if not exist .env (
    if exist .env.example (
        copy .env.example .env
        echo Created .env file from .env.example
        echo.
        echo IMPORTANT: Please edit .env file and add your Hugging Face API key
        echo Get your free API key from: https://huggingface.co/settings/tokens
    ) else (
        echo HF_API_KEY=your_huggingface_api_key_here > .env
        echo Created .env file
        echo.
        echo IMPORTANT: Please edit .env file and add your Hugging Face API key
        echo Get your free API key from: https://huggingface.co/settings/tokens
    )
) else (
    echo .env file already exists
)
echo.

echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Edit .env file and add your Hugging Face API key
echo 2. Run: python test_apis.py (to test your setup)
echo 3. Run: python Jarvis.py (to start Jarvis)
echo.
echo If you created a virtual environment, remember to activate it:
echo   venv\Scripts\activate.bat
echo.
pause
