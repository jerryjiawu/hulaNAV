@echo off
REM Create virtual environment with Python 3.6
echo Creating virtual environment...
py -3.6 -m venv venv-py36
if %errorlevel% neq 0 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

REM Activate virtual environment (IMPORTANT: use 'call' and '.bat')
echo Activating virtual environment...
call .\venv-py36\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

REM Install pyhula from wheel
echo Installing pyhula...
pip install .\hula\pyhula-1.1.6-cp36-cp36m-win_amd64.whl
if %errorlevel% neq 0 (
    echo ERROR: Failed to install pyhula
    pause
    exit /b 1
)

REM Install requirements
echo Installing requirements...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install requirements
    pause
    exit /b 1
)

echo.
echo Installation completed successfully!
echo To activate environment manually: .\venv-py36\Scripts\activate.bat
pause