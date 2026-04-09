from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
import math

app = FastAPI(title="Modern Calculator API")

class CalculationRequest(BaseModel):
    expression: str

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Modern Calculator</title>
        <style>
            :root {
                --bg: #0f172a;
                --surface: #1e293b;
                --surface-2: #334155;
                --accent: #38bdf8;
                --accent-2: #8b5cf6;
                --text: #e2e8f0;
                --muted: #94a3b8;
                --danger: #f87171;
                font-family: Inter, system-ui, sans-serif;
            }

            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                min-height: 100vh;
                display: grid;
                place-items: center;
                background: radial-gradient(circle at top, rgba(56, 189, 248, 0.16), transparent 32%),
                            radial-gradient(circle at bottom right, rgba(139, 92, 246, 0.18), transparent 28%),
                            var(--bg);
                color: var(--text);
            }

            .calculator {
                width: min(420px, calc(100vw - 2rem));
                border-radius: 32px;
                padding: 2rem;
                background: linear-gradient(180deg, rgba(15,23,42,0.98), rgba(30,41,59,0.95));
                box-shadow: 0 32px 80px rgba(0, 0, 0, 0.35);
                border: 1px solid rgba(148, 163, 184, 0.12);
            }

            .header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 1.5rem;
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

            button {
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

            button:hover {
                transform: translateY(-1px);
                background: rgba(148, 163, 184, 0.14);
            }

            button:active {
                transform: translateY(0);
                background: rgba(148, 163, 184, 0.2);
            }

            button.operator {
                background: linear-gradient(135deg, rgba(56, 189, 248, 0.22), rgba(139, 92, 246, 0.22));
                color: #eff6ff;
            }

            button.clear {
                background: rgba(248, 113, 113, 0.18);
                color: #fecaca;
            }

            button.equals {
                grid-column: span 2;
                background: linear-gradient(135deg, #38bdf8, #8b5cf6);
                color: #0f172a;
            }

            @media (max-width: 420px) {
                .calculator {
                    padding: 1.25rem;
                }

                .display {
                    min-height: 3.5rem;
                    font-size: 1.75rem;
                }

                button {
                    padding: 0.85rem;
                    font-size: 1rem;
                }
            }
        </style>
    </head>
    <body>
        <div class="calculator">
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

        <script>
            const display = document.getElementById('output');
            const history = document.getElementById('history');
            let expression = '';
            let justCalculated = false;

            const buttonElements = document.querySelectorAll('button[data-key]');
            buttonElements.forEach((button) => {
                button.addEventListener('click', () => {
                    const key = button.dataset.key;
                    handleKey(key);
                });
            });

            // Add keyboard support
            document.addEventListener('keydown', (event) => {
                const key = event.key;
                const keyMappings = {
                    '0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
                    '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
                    '+': '+', '-': '-', '*': '*', '/': '/', '^': '^',
                    '(': '(', ')': ')', '.': '.', '=': '=', 'Enter': '=',
                    'Escape': 'clear', 'Delete': 'clear', 'Backspace': 'clear'
                };

                if (keyMappings[key]) {
                    event.preventDefault(); // Prevent default browser behavior
                    handleKey(keyMappings[key]);
                }
            });

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

                // If we just calculated a result and user presses a number, start new expression
                if (justCalculated && !isNaN(key) && key !== '.') {
                    expression = key;
                    justCalculated = false;
                    updateDisplay();
                    return;
                }

                // If we just calculated and user presses an operator, continue with result
                if (justCalculated && ['+', '-', '*', '/', '^', '(', ')'].includes(key)) {
                    // Keep the current result and add the operator
                    justCalculated = false;
                    // expression is already the result, so just append the operator
                } else {
                    justCalculated = false;
                }

                expression += key;
                updateDisplay();
            }

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
