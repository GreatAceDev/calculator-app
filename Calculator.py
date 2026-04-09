from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import math

app = FastAPI(title="Ace")
app.mount("/static", StaticFiles(directory="Static"), name="static")

class CalculationRequest(BaseModel):
    expression: str

class TimeConversionRequest(BaseModel):
    value: float
    unit: str

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Ace</title>
        <style>
            :root {
                --bg: #0f172a;
                --surface: #1e293b;
                --surface-2: #334155;
                --accent: #38bdf8;
                --accent-2: #8b5cf6;
                --text: #e2e8f0;
                --muted: #94a3b8;
                --border: rgba(148, 163, 184, 0.18);
                font-family: 'Inter', system-ui, sans-serif;
            }

            * { box-sizing: border-box; }
            body {
                margin: 0;
                min-height: 100vh;
                background: radial-gradient(circle at top, rgba(56, 189, 248, 0.18), transparent 30%),
                            radial-gradient(circle at bottom right, rgba(139, 92, 246, 0.16), transparent 35%),
                            var(--bg);
                color: var(--text);
                overflow-x: hidden;
            }

            .hero {
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 2rem;
                position: relative;
                max-width: 1200px;
                margin: 0 auto;
            }

            .hero-content {
                flex: 1;
                text-align: center;
                z-index: 2;
                position: relative;
            }

            .logo {
                display: none;
            }

            .search-box {
                width: 100%;
                max-width: 500px;
                padding: 1rem 1.5rem;
                border-radius: 50px;
                background: rgba(30, 41, 59, 0.8);
                border: 2px solid rgba(56, 189, 248, 0.3);
                color: var(--text);
                font-size: 1rem;
                margin-bottom: 2rem;
                transition: border-color 0.2s ease;
            }

            .search-box:focus {
                outline: none;
                border-color: var(--accent);
                box-shadow: 0 0 20px rgba(56, 189, 248, 0.2);
            }

            .apps-section {
                width: 100%;
                margin-top: 4rem;
                padding-top: 3rem;
                border-top: 1px solid rgba(148, 163, 184, 0.16);
            }

            .apps-section h2 {
                font-size: 2rem;
                margin-bottom: 2rem;
                color: var(--text);
                text-align: center;
            }

            .tabs {
                display: flex;
                gap: 1rem;
                justify-content: center;
                flex-wrap: wrap;
                margin-bottom: 3rem;
            }

            .tab-btn {
                padding: 0.8rem 1.5rem;
                border-radius: 25px;
                border: 2px solid rgba(56, 189, 248, 0.3);
                background: transparent;
                color: var(--text);
                cursor: pointer;
                font-weight: 600;
                transition: all 0.2s ease;
            }

            .tab-btn:hover {
                border-color: var(--accent);
                background: rgba(56, 189, 248, 0.1);
            }

            .tab-btn.active {
                background: linear-gradient(135deg, var(--accent), var(--accent-2));
                border-color: transparent;
                color: var(--bg);
            }

            .app-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 2rem;
                margin-bottom: 3rem;
            }

            .app-card {
                border-radius: 16px;
                background: linear-gradient(180deg, rgba(30,41,59,0.6), rgba(15,23,42,0.8));
                border: 1px solid rgba(148, 163, 184, 0.12);
                padding: 1.5rem;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }

            .app-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 15px 40px rgba(56, 189, 248, 0.15);
                border-color: rgba(56, 189, 248, 0.3);
            }

            .app-title {
                font-size: 1.3rem;
                font-weight: 700;
                margin-bottom: 0.5rem;
                color: var(--text);
            }

            .app-description {
                font-size: 0.95rem;
                color: var(--muted);
                margin-bottom: 1.5rem;
                line-height: 1.5;
            }

            .app-download-btn {
                padding: 0.8rem 1.5rem;
                border-radius: 20px;
                background: linear-gradient(135deg, var(--accent), var(--accent-2));
                color: var(--bg);
                border: none;
                font-weight: 600;
                cursor: pointer;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }

            .app-download-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 25px rgba(56, 189, 248, 0.3);
            }

            .brand {
                font-family: 'Brush Script MT', cursive;
                font-size: clamp(4rem, 12vw, 8rem);
                font-weight: normal;
                background: linear-gradient(135deg, var(--accent), var(--accent-2));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                margin: 0 0 1rem;
                letter-spacing: 0.1em;
            }

            .tagline {
                font-size: 1.4rem;
                color: var(--muted);
                margin: 0 0 3rem;
                max-width: 600px;
                line-height: 1.6;
            }

            .cta-button {
                padding: 1.2rem 2.5rem;
                border-radius: 50px;
                background: linear-gradient(135deg, var(--accent), var(--accent-2));
                color: var(--bg);
                font-weight: 700;
                font-size: 1.2rem;
                text-decoration: none;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 18px 40px rgba(56, 189, 248, 0.15);
                transition: transform 0.2s ease, box-shadow 0.2s ease;
                cursor: pointer;
                border: none;
            }

            .cta-button:hover {
                transform: translateY(-2px);
                box-shadow: 0 25px 60px rgba(56, 189, 248, 0.25);
            }

            .calculator-section {
                display: none;
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(15, 23, 42, 0.95);
                backdrop-filter: blur(10px);
                z-index: 1000;
                justify-content: center;
                align-items: center;
                padding: 2rem;
            }

            .calculator-section.show {
                display: flex;
            }

            .calculator {
                width: min(420px, calc(100vw - 2rem));
                border-radius: 32px;
                padding: 2rem;
                background: linear-gradient(180deg, rgba(15,23,42,0.98), rgba(30,41,59,0.95));
                box-shadow: 0 32px 80px rgba(0, 0, 0, 0.35);
                border: 1px solid rgba(148, 163, 184, 0.12);
                position: relative;
            }

            .close-btn {
                position: absolute;
                top: 1rem;
                right: 1rem;
                background: rgba(248, 113, 113, 0.18);
                color: #fecaca;
                border: none;
                border-radius: 50%;
                width: 40px;
                height: 40px;
                cursor: pointer;
                font-size: 1.2rem;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 1.5rem;
                gap: 1rem;
            }

            .header h1 {
                font-size: 1.4rem;
                letter-spacing: 0.04em;
                margin: 0;
            }

            .display {
                width: 100%;
                min-height: 4.5rem;
                border-radius: 1.5rem;
                padding: 1rem 1.25rem;
                margin-bottom: 1.5rem;
                background: rgba(15, 23, 42, 0.8);
                border: 1px solid rgba(148, 163, 184, 0.16);
                color: var(--text);
                font-size: 2rem;
                text-align: right;
                letter-spacing: 0.02em;
                display: grid;
                place-content: center end;
                word-break: break-all;
            }

            .display .subtext {
                color: var(--muted);
                font-size: 0.85rem;
            }

            .keypad {
                display: grid;
                gap: 0.85rem;
                grid-template-columns: repeat(4, minmax(0, 1fr));
            }

            .calculator button {
                border: none;
                border-radius: 18px;
                padding: 1rem;
                font-size: 1.1rem;
                font-weight: 600;
                color: var(--text);
                background: rgba(148, 163, 184, 0.08);
                cursor: pointer;
                transition: transform 0.15s ease, background 0.15s ease, box-shadow 0.15s ease;
                box-shadow: inset 0 0 0 1px rgba(148, 163, 184, 0.06);
            }

            .calculator button:hover {
                transform: translateY(-1px);
                background: rgba(148, 163, 184, 0.14);
            }

            .calculator button:active {
                transform: translateY(0);
                background: rgba(148, 163, 184, 0.2);
            }

            .calculator button.operator {
                background: linear-gradient(135deg, rgba(56, 189, 248, 0.22), rgba(139, 92, 246, 0.22));
                color: #eff6ff;
            }

            .calculator button.clear {
                background: rgba(248, 113, 113, 0.18);
                color: #fecaca;
            }

            .calculator button.equals {
                grid-column: span 2;
                background: linear-gradient(135deg, #38bdf8, #8b5cf6);
                color: #0f172a;
            }

            .time-converter-section {
                display: none;
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(15, 23, 42, 0.95);
                backdrop-filter: blur(10px);
                z-index: 1000;
                justify-content: center;
                align-items: center;
                padding: 2rem;
            }

            .time-converter-section.show {
                display: flex;
            }

            .time-converter {
                width: min(500px, calc(100vw - 2rem));
                border-radius: 32px;
                padding: 2rem;
                background: linear-gradient(180deg, rgba(15,23,42,0.98), rgba(30,41,59,0.95));
                box-shadow: 0 32px 80px rgba(0, 0, 0, 0.35);
                border: 1px solid rgba(148, 163, 184, 0.12);
                position: relative;
            }

            .time-converter .close-btn {
                position: absolute;
                top: 1rem;
                right: 1rem;
                background: rgba(248, 113, 113, 0.18);
                color: #fecaca;
                border: none;
                border-radius: 50%;
                width: 40px;
                height: 40px;
                cursor: pointer;
                font-size: 1.2rem;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .time-converter .header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 1.5rem;
                gap: 1rem;
            }

            .time-converter .header h1 {
                font-size: 1.4rem;
                letter-spacing: 0.04em;
                margin: 0;
            }

            .time-input-section {
                margin-bottom: 1.5rem;
            }

            .time-input-group {
                display: flex;
                gap: 1rem;
                margin-bottom: 1rem;
                align-items: center;
            }

            .time-input-group label {
                min-width: 80px;
                color: var(--text);
                font-weight: 600;
            }

            .time-input {
                flex: 1;
                padding: 0.8rem;
                border-radius: 8px;
                background: rgba(15, 23, 42, 0.8);
                border: 1px solid rgba(148, 163, 184, 0.16);
                color: var(--text);
                font-size: 1rem;
            }

            .time-input:focus {
                outline: none;
                border-color: var(--accent);
            }

            .convert-btn {
                width: 100%;
                padding: 1rem;
                border-radius: 12px;
                background: linear-gradient(135deg, var(--accent), var(--accent-2));
                color: var(--bg);
                border: none;
                font-weight: 600;
                cursor: pointer;
                transition: transform 0.2s ease;
            }

            .convert-btn:hover {
                transform: translateY(-2px);
            }

            .results-section {
                margin-top: 1.5rem;
                padding: 1rem;
                border-radius: 12px;
                background: rgba(15, 23, 42, 0.6);
                border: 1px solid rgba(148, 163, 184, 0.12);
            }

            .result-item {
                display: flex;
                justify-content: space-between;
                padding: 0.5rem 0;
                border-bottom: 1px solid rgba(148, 163, 184, 0.08);
            }

            .result-item:last-child {
                border-bottom: none;
            }

            .result-label {
                color: var(--muted);
            }

            .result-value {
                color: var(--text);
                font-weight: 600;
            }

            @media (max-width: 768px) {
                .hero {
                    flex-direction: column;
                    text-align: center;
                }

                .hero-content {
                    margin-right: 0;
                    margin-top: 2rem;
                }

                .logo {
                    width: 250px;
                    height: 250px;
                    top: -30px;
                    left: -30px;
                }
            }

            @media (max-width: 420px) {
                .calculator {
                    padding: 1.25rem;
                }

                .display {
                    min-height: 3.5rem;
                    font-size: 1.75rem;
                }

                .calculator button {
                    padding: 0.85rem;
                    font-size: 1rem;
                }

                .logo {
                    width: 200px;
                    height: 200px;
                    top: -20px;
                    left: -20px;
                }
            }
        </style>
    </head>
    <body>
        <div class="hero">
            <div class="hero-content">
                <h1 class="brand">Ace</h1>
                <p class="tagline">Your hub for amazing apps and tools. Discover, download, and create.</p>
                <input type="text" class="search-box" id="searchBox" placeholder="Search apps..." />
                <button class="cta-button" onclick="showCalculator()">Use Calculator</button>
            </div>
        </div>

        <div class="apps-section">
            <h2>Featured Apps</h2>
            <div class="tabs">
                <button class="tab-btn active" onclick="filterApps('all')">All Apps</button>
                <button class="tab-btn" onclick="filterApps('tools')">Tools</button>
                <button class="tab-btn" onclick="filterApps('games')">Games</button>
                <button class="tab-btn" onclick="filterApps('utilities')">Utilities</button>
            </div>
            <div class="app-grid" id="appGrid">
                <div class="app-card" data-category="tools">
                    <div class="app-title">Modern Calculator</div>
                    <div class="app-description">A powerful calculator with keyboard support and API integration.</div>
                    <button class="app-download-btn" onclick="showCalculator()">Use Now</button>
                </div>
                <div class="app-card" data-category="tools">
                    <div class="app-title">Text Converter</div>
                    <div class="app-description">Convert between different text formats and encodings.</div>
                    <button class="app-download-btn" onclick="alert('Coming Soon!')">Download</button>
                </div>
                <div class="app-card" data-category="utilities">
                    <div class="app-title">Universal Time Converter</div>
                    <div class="app-description">Convert between days, hours, minutes, months, and years with precision.</div>
                    <button class="app-download-btn" onclick="showTimeConverter()">Use Now</button>
                </div>
                    <div class="app-title">Sample Game</div>
                    <div class="app-description">Fun browser-based game available for download.</div>
                    <button class="app-download-btn" onclick="alert('Coming Soon!')">Download</button>
                </div>
            </div>
        </div>

        <div class="calculator-section" id="calculatorSection">
            <div class="calculator">
                <button class="close-btn" onclick="hideCalculator()">×</button>
                <div class="header">
                    <div>
                        <h1>Modern Calculator</h1>
                        <p style="margin: 0.25rem 0 0; color: var(--muted); font-size: 0.95rem;">Powered by FastAPI</p>
                    </div>
                    <div style="text-align: right; color: var(--muted); font-size: 0.9rem;">API-driven UX</div>
                </div>
                <div class="display" id="display">
                    <div class="subtext" id="history">Ready</div>
                    <div id="output">0</div>
                </div>
                <div class="keypad">
                    <button class="clear" data-key="clear">AC</button>
                    <button class="operator" data-key="(">(</button>
                    <button class="operator" data-key=")">)</button>
                    <button class="operator" data-key="/">÷</button>
                    <button data-key="7">7</button>
                    <button data-key="8">8</button>
                    <button data-key="9">9</button>
                    <button class="operator" data-key="*">×</button>
                    <button data-key="4">4</button>
                    <button data-key="5">5</button>
                    <button data-key="6">6</button>
                    <button class="operator" data-key="-">−</button>
                    <button data-key="1">1</button>
                    <button data-key="2">2</button>
                    <button data-key="3">3</button>
                    <button class="operator" data-key="+">+</button>
                    <button data-key="0">0</button>
                    <button data-key=".">.</button>
                    <button class="operator" data-key="^">^</button>
                    <button class="equals" data-key="=">=</button>
                </div>
            </div>
        </div>

        <div class="time-converter-section" id="timeConverterSection">
            <div class="time-converter">
                <button class="close-btn" onclick="hideTimeConverter()">×</button>
                <div class="header">
                    <div>
                        <h1>Universal Time Converter</h1>
                        <p style="margin: 0.25rem 0 0; color: var(--muted); font-size: 0.95rem;">Ace Edition</p>
                    </div>
                    <div style="text-align: right; color: var(--muted); font-size: 0.9rem;">Precision Time Math</div>
                </div>
                <div class="time-input-section">
                    <div class="time-input-group">
                        <label for="timeValue">Value:</label>
                        <input type="number" id="timeValue" class="time-input" placeholder="Enter value" step="any">
                    </div>
                    <div class="time-input-group">
                        <label for="timeUnit">From:</label>
                        <select id="timeUnit" class="time-input">
                            <option value="days">Days</option>
                            <option value="hours">Hours</option>
                            <option value="minutes">Minutes</option>
                            <option value="months">Months</option>
                            <option value="years">Years</option>
                        </select>
                    </div>
                    <button class="convert-btn" onclick="convertTime()">Convert Time</button>
                </div>
                <div class="results-section" id="resultsSection" style="display: none;">
                    <h3 style="margin: 0 0 1rem; color: var(--text);">Conversion Results:</h3>
                    <div id="resultsList"></div>
                </div>
            </div>
        </div>

        <script>
            const display = document.getElementById('output');
            const history = document.getElementById('history');
            const searchBox = document.getElementById('searchBox');
            let expression = '';
            let justCalculated = false;
            let currentFilter = 'all';

            const buttonElements = document.querySelectorAll('button[data-key]');
            buttonElements.forEach((button) => {
                button.addEventListener('click', () => {
                    const key = button.dataset.key;
                    handleKey(key);
                });
            });

            searchBox.addEventListener('input', (e) => {
                const searchTerm = e.target.value.toLowerCase();
                const cards = document.querySelectorAll('.app-card');
                cards.forEach(card => {
                    const title = card.querySelector('.app-title').textContent.toLowerCase();
                    const description = card.querySelector('.app-description').textContent.toLowerCase();
                    const matches = title.includes(searchTerm) || description.includes(searchTerm);
                    card.style.display = matches ? 'block' : 'none';
                });
            });

            // Time converter input Enter key support
            document.getElementById('timeValue').addEventListener('keydown', (event) => {
                if (event.key === 'Enter') {
                    convertTime();
                }
            });

            function filterApps(category) {
                currentFilter = category;
                const cards = document.querySelectorAll('.app-card');
                const buttons = document.querySelectorAll('.tab-btn');
                
                buttons.forEach(btn => btn.classList.remove('active'));
                event.target.classList.add('active');
                
                cards.forEach(card => {
                    if (category === 'all' || card.dataset.category === category) {
                        card.style.display = 'block';
                    } else {
                        card.style.display = 'none';
                    }
                });
            }

            function showCalculator() {
                document.getElementById('calculatorSection').classList.add('show');
            }

            function hideCalculator() {
                document.getElementById('calculatorSection').classList.remove('show');
            }

            function showTimeConverter() {
                document.getElementById('timeConverterSection').classList.add('show');
            }

            function hideTimeConverter() {
                document.getElementById('timeConverterSection').classList.remove('show');
                // Reset form
                document.getElementById('timeValue').value = '';
                document.getElementById('timeUnit').value = 'days';
                document.getElementById('resultsSection').style.display = 'none';
            }

            function convertTime() {
                const value = parseFloat(document.getElementById('timeValue').value);
                const unit = document.getElementById('timeUnit').value;
                
                if (isNaN(value) || value <= 0) {
                    alert('Please enter a valid positive number');
                    return;
                }
                
                // Call the API endpoint
                fetch('/api/convert-time', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ value: value, unit: unit })
                })
                .then(response => {
                    if (!response.ok) {
                        return response.json().then(err => {
                            throw new Error(err.detail || 'Conversion failed');
                        });
                    }
                    return response.json();
                })
                .then(data => {
                    // Display results
                    const resultsList = document.getElementById('resultsList');
                    resultsList.innerHTML = `
                        <div class="result-item">
                            <span class="result-label">Days:</span>
                            <span class="result-value">${data.days}</span>
                        </div>
                        <div class="result-item">
                            <span class="result-label">Hours:</span>
                            <span class="result-value">${data.hours}</span>
                        </div>
                        <div class="result-item">
                            <span class="result-label">Minutes:</span>
                            <span class="result-value">${data.minutes}</span>
                        </div>
                        <div class="result-item">
                            <span class="result-label">Seconds:</span>
                            <span class="result-value">${data.seconds}</span>
                        </div>
                        <div class="result-item">
                            <span class="result-label">Months:</span>
                            <span class="result-value">${data.months}</span>
                        </div>
                        <div class="result-item">
                            <span class="result-label">Years:</span>
                            <span class="result-value">${data.years}</span>
                        </div>
                    `;
                    
                    document.getElementById('resultsSection').style.display = 'block';
                })
                .catch(error => {
                    alert('Error: ' + error.message);
                });
            }

            function updateDisplay() {
                display.textContent = expression || '0';
            }

            function handleKey(key) {
                if (key === 'clear') {
                    expression = '';
                    history.textContent = 'Ready';
                    justCalculated = false;
                    updateDisplay();
                    return;
                }

                if (key === '=') {
                    if (!expression.trim()) {
                        return;
                    }
                    history.textContent = expression;
                    evaluateExpression(expression);
                    return;
                }

                if (justCalculated && !isNaN(key) && key !== '.') {
                    expression = key;
                    justCalculated = false;
                    updateDisplay();
                    return;
                }

                if (justCalculated && ['+', '-', '*', '/', '^', '(', ')'].includes(key)) {
                    justCalculated = false;
                } else {
                    justCalculated = false;
                }

                expression += key;
                updateDisplay();
            }

            document.addEventListener('keydown', (event) => {
                const accepted = ['0','1','2','3','4','5','6','7','8','9','+','-','*','/','^','(',')','.','=','Enter','Escape','Delete','Backspace'];
                if (!accepted.includes(event.key)) {
                    return;
                }
                event.preventDefault();
                const keyMappings = {
                    'Enter': '=',
                    'Escape': 'clear',
                    'Delete': 'clear',
                    'Backspace': 'clear'
                };
                handleKey(keyMappings[event.key] || event.key);
            });

            async function evaluateExpression(expr) {
                try {
                    const response = await fetch('/api/evaluate', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ expression: expr }),
                    });

                    if (!response.ok) {
                        const errorData = await response.json();
                        throw new Error(errorData.detail || 'Failed to evaluate');
                    }

                    const data = await response.json();
                    expression = String(data.result);
                    justCalculated = true;
                    updateDisplay();
                    history.textContent = expr + ' =';
                } catch (error) {
                    display.textContent = 'Error';
                    history.textContent = error.message;
                    expression = '';
                    justCalculated = false;
                }
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


def compute_result(expression: str):
    normalized = expression.replace('×', '*').replace('÷', '/').replace('^', '**')
    allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith('_')}
    allowed_names.update({
        'abs': abs,
        'round': round,
        'min': min,
        'max': max,
    })
    result = eval(normalized, {'__builtins__': {}}, allowed_names)
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    return result


def convert_time(value: float, unit: str):
    unit = unit.lower()
    
    # Convert to base unit (days)
    if unit == 'days':
        days = value
    elif unit == 'hours':
        days = value / 24
    elif unit == 'minutes':
        days = value / 1440  # 24 * 60
    elif unit == 'months':
        days = value * 30.44  # Average month
    elif unit == 'years':
        days = value * 365.25  # Average year with leap years
    else:
        raise ValueError(f"Invalid unit: {unit}")
    
    # Convert from days to all other units
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    months = days / 30.44
    years = days / 365.25
    
    return {
        'days': round(days, 4),
        'hours': round(hours, 2),
        'minutes': round(minutes, 2),
        'seconds': round(seconds, 2),
        'months': round(months, 4),
        'years': round(years, 4)
    }


@app.get("/ap/calc")
def calc(expression: str):
    expression = expression.strip()
    if not expression:
        raise HTTPException(status_code=400, detail="Expression is required.")

    try:
        result = compute_result(expression)
        return JSONResponse(content={"result": result})
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Invalid expression: {exc}")


@app.post("/api/evaluate")
def evaluate(request: CalculationRequest):
    expression = request.expression.strip()
    if not expression:
        raise HTTPException(status_code=400, detail="Expression is required.")

    try:
        result = compute_result(expression)
        return JSONResponse(content={"result": result})
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Invalid expression: {exc}")


@app.post("/api/convert-time")
def convert_time_endpoint(request: TimeConversionRequest):
    if request.value <= 0:
        raise HTTPException(status_code=400, detail="Value must be positive.")
    
    valid_units = ['days', 'hours', 'minutes', 'months', 'years']
    if request.unit.lower() not in valid_units:
        raise HTTPException(status_code=400, detail=f"Invalid unit. Must be one of: {', '.join(valid_units)}")
    
    try:
        result = convert_time(request.value, request.unit)
        return JSONResponse(content=result)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Conversion error: {exc}")
