const display = document.getElementById('output');
const history = document.getElementById('history');
let expression = '';

const buttonElements = document.querySelectorAll('button[data-key]');
buttonElements.forEach((button) => {
    button.addEventListener('click', () => {
        const key = button.dataset.key;
        handleKey(key);
    });
});

function updateDisplay() {
    display.textContent = expression || '0';
}

function handleKey(key) {
    if (key === 'clear') {
        expression = '';
        history.textContent = 'Ready';
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
        updateDisplay();
        history.textContent = expr + ' =';
    } catch (error) {
        display.textContent = 'Error';
        history.textContent = error.message;
        expression = '';
    }
}
