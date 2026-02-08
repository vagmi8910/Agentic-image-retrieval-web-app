@echo off
echo Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error installing dependencies!
    pause
    exit /b %errorlevel%
)

echo Starting Agentic Image Retrieval System...
streamlit run app.py
pause
