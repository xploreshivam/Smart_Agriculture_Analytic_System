@echo off
echo Starting Smart Agriculture System...
cd /d "%~dp0"

:: Activate virtual environment if it exists
if exist venv\Scripts\activate (
    echo Activating Virtual Environment...
    call venv\Scripts\activate
)

:: Run the application
echo Launching Flask Server on http://127.0.0.1:5001
py app.py || python app.py

pause
