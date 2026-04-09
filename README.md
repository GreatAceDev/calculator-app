# Modern Calculator

A beautiful, responsive calculator built with FastAPI and modern web technologies.

## Features

- ✅ Modern glassmorphism UI design
- ✅ Basic math operations (+, -, ×, ÷, ^)
- ✅ Parentheses support
- ✅ Keyboard and mouse input
- ✅ Smart input handling (prevents accidental number appending)
- ✅ API endpoints for programmatic access

## Live Demo

Visit the live calculator at: [Your Railway URL - add it here]

## How to Run Locally

### Prerequisites
- Python 3.8 or higher
- Internet connection (for initial setup)

### Installation

1. **Download the project**
   - Download the ZIP file from GitHub
   - Extract it to a folder on your computer

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the calculator**
   ```bash
   python -m uvicorn Calculator:app --reload --port 8000
   ```

4. **Open in browser**
   - Go to: `http://127.0.0.1:8000`
   - Start calculating!

### Keyboard Shortcuts
- Numbers: `0-9`
- Operators: `+`, `-`, `*`, `/`, `^`
- Parentheses: `(`, `)`
- Decimal: `.`
- Equals: `=` or `Enter`
- Clear: `Escape`, `Delete`, or `Backspace`

## API Usage

The calculator also provides API endpoints:

### Calculate Expression
```bash
curl "http://127.0.0.1:8000/ap/calc?expression=2+3*4"
```

### POST Endpoint
```bash
curl -X POST "http://127.0.0.1:8000/api/evaluate" \
     -H "Content-Type: application/json" \
     -d '{"expression": "2+3*4"}'
```

## Project Structure

```
calculator-app/
├── Calculator.py          # FastAPI backend
├── requirements.txt       # Python dependencies
├── Procfile              # Railway deployment
├── runtime.txt           # Python version for Railway
├── Static/
│   ├── Index.html        # Calculator UI
│   └── Script.js         # Frontend logic
└── README.md             # This file
```

## Built With

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with glassmorphism effects
- **Deployment**: Railway (optional)

## Contributing

Feel free to fork this project and add your own features!

## License

This project is open source and available under the MIT License.

A 14-year-old Python learner! 🚀