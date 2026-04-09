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
        <title>The Great Ace Hub</title>
        <style>
            :root {
                --bg: #ffffff;
                --surface: #f8fafc;
                --surface-2: #e2e8f0;
                --accent: #3b82f6;
                --accent-2: #8b5cf6;
                --text: #1e293b;
                --muted: #64748b;
                --border: rgba(100, 116, 139, 0.2);
                font-family: 'Inter', system-ui, sans-serif;
            }

            .site-header {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                z-index: 1000;
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                border-bottom: 1px solid rgba(100, 116, 139, 0.1);
                padding: 1rem 2rem;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            }

            .logo-container {
                display: flex;
                align-items: center;
            }

            .site-logo {
                height: 60px;
                width: auto;
                object-fit: contain;
            }

            * { box-sizing: border-box; }
            body {
                margin: 0;
                min-height: 100vh;
                background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
                color: var(--text);
                overflow-x: hidden;
            }

            .hero {
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 6rem 2rem 2rem;
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
                background: rgba(241, 245, 249, 0.8);
                border: 2px solid rgba(59, 130, 246, 0.3);
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
                background: linear-gradient(180deg, rgba(248,250,252,0.8), rgba(226,232,240,0.9));
                border: 1px solid rgba(100, 116, 139, 0.2);
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

            .sonic-section {
                margin-top: 3rem;
                padding: 1rem;
                border-radius: 20px;
                background: rgba(248, 250, 252, 0.95);
                border: 1px solid rgba(100, 116, 139, 0.15);
            }

            .sonic-toggle-btn {
                width: 100%;
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 1rem 1.25rem;
                border-radius: 16px;
                background: #ffffff;
                border: 1px solid rgba(100, 116, 139, 0.2);
                cursor: pointer;
                font-size: 1rem;
                font-weight: 700;
                color: var(--text);
                transition: background 0.2s ease, transform 0.2s ease;
            }

            .sonic-toggle-btn:hover {
                background: #f1f5f9;
                transform: translateY(-1px);
            }

            .sonic-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
                gap: 1rem;
                margin-top: 1rem;
            }

            .sonic-card {
                padding: 1rem;
                border-radius: 18px;
                background: linear-gradient(180deg, rgba(255,255,255,0.95), rgba(241,245,249,0.95));
                border: 1px solid rgba(100, 116, 139, 0.15);
                box-shadow: 0 10px 30px rgba(15, 23, 42, 0.05);
            }

            .sonic-card h3 {
                margin: 0 0 0.5rem;
                color: var(--text);
            }

            .sonic-card p {
                margin: 0 0 1rem;
                color: var(--muted);
                line-height: 1.5;
            }

            .sonic-link {
                display: inline-flex;
                align-items: center;
                padding: 0.8rem 1rem;
                border-radius: 14px;
                background: linear-gradient(135deg, var(--accent), var(--accent-2));
                color: #ffffff;
                text-decoration: none;
                font-weight: 600;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }

            .sonic-link:hover {
                transform: translateY(-1px);
                box-shadow: 0 10px 20px rgba(59, 130, 246, 0.2);
            }

            .toggle-icon {
                font-size: 1.2rem;
                transition: transform 0.2s ease;
            }

            .toggle-icon.open {
                transform: rotate(180deg);
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
                background: rgba(255, 255, 255, 0.95);
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
                background: linear-gradient(180deg, rgba(248,250,252,0.98), rgba(226,232,240,0.95));
                box-shadow: 0 32px 80px rgba(0, 0, 0, 0.15);
                border: 1px solid rgba(100, 116, 139, 0.2);
                position: relative;
            }

            .close-btn {
                position: absolute;
                top: 1rem;
                right: 1rem;
                background: rgba(239, 68, 68, 0.15);
                color: #dc2626;
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
                background: rgba(241, 245, 249, 0.8);
                border: 1px solid rgba(100, 116, 139, 0.2);
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
                background: rgba(241, 245, 249, 0.8);
                cursor: pointer;
                transition: transform 0.15s ease, background 0.15s ease, box-shadow 0.15s ease;
                box-shadow: inset 0 0 0 1px rgba(100, 116, 139, 0.2);
            }

            .calculator button:hover {
                transform: translateY(-1px);
                background: rgba(241, 245, 249, 0.9);
            }

            .calculator button:active {
                transform: translateY(0);
                background: rgba(226, 232, 240, 0.9);
            }

            .calculator button.operator {
                background: linear-gradient(135deg, rgba(59, 130, 246, 0.15), rgba(139, 92, 246, 0.15));
                color: var(--text);
            }

            .calculator button.clear {
                background: rgba(239, 68, 68, 0.15);
                color: #dc2626;
            }

            .calculator button.equals {
                grid-column: span 2;
                background: linear-gradient(135deg, #3b82f6, #8b5cf6);
                color: #ffffff;
            }

            .time-converter-section {
                display: none;
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(255, 255, 255, 0.95);
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
                background: linear-gradient(180deg, rgba(248,250,252,0.98), rgba(226,232,240,0.95));
                box-shadow: 0 32px 80px rgba(0, 0, 0, 0.15);
                border: 1px solid rgba(100, 116, 139, 0.2);
                position: relative;
            }

            .time-converter .close-btn {
                position: absolute;
                top: 1rem;
                right: 1rem;
                background: rgba(239, 68, 68, 0.15);
                color: #dc2626;
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
                background: rgba(241, 245, 249, 0.8);
                border: 1px solid rgba(100, 116, 139, 0.2);
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
                background: rgba(241, 245, 249, 0.6);
                border: 1px solid rgba(100, 116, 139, 0.2);
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
        <header class="site-header">
            <div class="logo-container">
                <img src="/static/Untitled_design__2_2.04-removebg-preview.png" alt="Ace Hub Logo" class="site-logo" onerror="console.log('Logo failed to load')">
            </div>
        </header>
        <div class="hero">
            <div class="hero-content">
                <h1 class="brand">The Great Ace Hub</h1>
                <p class="tagline">Your hub for amazing apps and tools. Discover, download, and create.</p>
                <input type="text" class="search-box" id="searchBox" placeholder="Search apps..." onkeyup="filterApps(this.value)"
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
                <div class="app-card" data-category="games">
                    <div class="app-title">Sample Game</div>
                    <div class="app-description">Fun browser-based game available for download.</div>
                    <button class="app-download-btn" onclick="alert('Coming Soon!')">Download</button>
                </div>
            </div>
        </div>

        <div class="sonic-section">
            <button class="sonic-toggle-btn" onclick="toggleSonicGames()">
                <h2>Check Out These Sonic Fan Games</h2>
                <span class="toggle-icon">▼</span>
            </button>
            <div class="sonic-grid" id="sonicGrid" style="display: none;">
                <div class="sonic-card">
                    <h3>Moon Facility</h3>
                    <p>A challenging Sonic fan game with unique levels and mechanics.</p>
                    <a href="https://moonfacility.com" target="_blank" class="sonic-link">Visit Moon Facility</a>
                </div>
                <div class="sonic-card">
                    <h3>Fallen Star</h3>
                    <p>An epic Sonic adventure with story-driven gameplay.</p>
                    <a href="https://fallenstarsonic.com" target="_blank" class="sonic-link">Visit Fallen Star</a>
                </div>
                <div class="sonic-card">
                    <h3>SRB2 (Sonic Robo Blast 2)</h3>
                    <p>The classic 3D Sonic fan game with multiplayer and custom levels.</p>
                    <a href="https://srb2.org" target="_blank" class="sonic-link">Visit SRB2</a>
                </div>
                <div class="sonic-card">
                    <h3>SRB2 Kart</h3>
                    <p>Racing fun with Sonic characters in this kart racing spin-off.</p>
                    <a href="https://srb2.org/kart" target="_blank" class="sonic-link">Visit SRB2 Kart</a>
                </div>
            </div>
        </div>

        <div class="footer-section">
            <div class="footer-content">
                <div class="footer-links">
                    <h3>Connect & Download</h3>
                    <div class="social-links">
                        <a href="https://github.com/GreatAceDev" target="_blank" class="social-link github">
                            <span>🐙</span> GitHub - Get the Apps
                        </a>
                        <a href="https://github.com/GreatAceDev/calculator-app" target="_blank" class="social-link">
                            <span>📱</span> Ace App Hub Source
                        </a>
                        <a href="https://discord.gg/sonic" target="_blank" class="social-link">
                            <span>💬</span> Sonic Community Discord
                        </a>
                        <a href="https://twitter.com/sonic" target="_blank" class="social-link">
                            <span>🐦</span> Follow Sonic News
                        </a>
                    </div>
                </div>
                <div class="footer-info">
                    <p>&copy; 2026 Ace App Hub. Made with ❤️ for the Sonic community.</p>
                    <p>Built with FastAPI, featuring calculator and time converter tools.</p>
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

            function filterApps() {
    // 1. Get the search text and clean it up
    const input = document.getElementById('searchBox');
    if (!input) return;
    const filter = input.value.toLowerCase().trim();

    // 2. Find every "Featured App" container
    // We search for 'div' because it's a safe bet for your cards
    const cards = document.querySelectorAll('.featured-grid div, .app-card');

    cards.forEach(card => {
        // Only filter actual card elements (the ones with text inside)
        if (card.innerText && card.innerText.length > 1) {
            const text = card.innerText.toLowerCase();
            
            // Show the card if it contains the search text
            if (text.includes(filter)) {
                card.style.display = ""; // Standard display
            } else {
                card.style.display = "none"; // Hide it
            }
        }
    });
}

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

            function toggleSonicGames() {
                const sonicGrid = document.getElementById('sonicGrid');
                const icon = document.querySelector('.toggle-icon');
                const isHidden = sonicGrid.style.display === 'none' || sonicGrid.style.display === '';
                sonicGrid.style.display = isHidden ? 'grid' : 'none';
                icon.classList.toggle('open', isHidden);
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
