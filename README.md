# Modern Calculator

A beautiful, responsive calculator built with FastAPI and modern web technologies.

## Features

- ✅ Modern glassmorphism UI design
- ✅ Basic math operations (+, -, ×, ÷, ^)
- ✅ Parentheses support
- ✅ Keyboard and mouse input
- ✅ Smart input handling (prevents accidental number appending)
- ✅ API endpoints for programmatic access

## How to Run

### 1. Install Python
Make sure you have Python 3.8+ installed. Download from [python.org](https://python.org).

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Calculator
```bash
python -m uvicorn Calculator:app --reload --port 8000
```

### 4. Open in Browser
Go to: `http://127.0.0.1:8000`

## API Endpoints

- `GET /` - Calculator web interface
- `GET /ap/calc?expression=1+2` - Calculate via URL
- `POST /api/evaluate` - Calculate via JSON API

Example API usage:
```bash
curl "http://127.0.0.1:8000/ap/calc?expression=2*3"
```

## Files

- `Calculator.py` - FastAPI backend with embedded HTML/CSS/JS
- `requirements.txt` - Python dependencies
- `Static/` - Alternative static files (not needed for main app)

## Built By

A 14-year-old Python learner! 🚀