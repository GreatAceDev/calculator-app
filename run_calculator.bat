@echo off
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting calculator...
python -m uvicorn Calculator:app --reload --port 8000
echo.
echo Calculator is running at: http://127.0.0.1:8000
echo Press Ctrl+C to stop
pause