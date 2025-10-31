@echo off
echo ================================================
echo   arXiv Paper Search - Starting Backend Server
echo ================================================
echo.
echo Checking Python installation...

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo X Python is not installed. Please install Python 3 first.
    pause
    exit /b 1
)

echo √ Python found
echo.
echo Installing/checking required packages...
python -m pip install flask flask-cors requests --quiet

echo √ All packages ready
echo.
echo ================================================
echo   Starting Server...
echo ================================================
echo.
echo The server will run at: http://localhost:5000
echo Now open arxiv-search.html in your browser!
echo.
echo Press Ctrl+C to stop the server
echo.

python arxiv_server.py
pause
