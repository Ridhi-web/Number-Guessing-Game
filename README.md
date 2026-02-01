# Number Guessing Game

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg">
  <img src="https://img.shields.io/badge/Streamlit-1.28+-red.svg">
  <img src="https://img.shields.io/badge/License-MIT-green.svg">
</div>

<div align="center">
  <h3>Interactive number guessing game with cosmic-themed UI</h3>
</div>

## Features

- **Three Difficulty Levels**: Easy (1-50), Medium (1-100), Hard (1-200)
- **Modern UI**: Cosmic theme with gradient backgrounds and responsive design
- **Statistics Tracking**: Win rate, total score, and games played
- **Smart Hints**: Hot/Cold feedback system with directional guidance

## Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation
```bash
git clone <repository-url>
cd number-guessing-game
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

### Running
```bash
streamlit run app.py  # Web version
python game.py        # Console version
```

## How to Play

1. Select difficulty level
2. Guess numbers within the range
3. Follow hints: Very Close (≤5), Warm (≤10), Cold (>10)
4. Score points based on remaining attempts + difficulty bonus

## Project Structure

```
number-guessing-game/
├── app.py              # Streamlit web app
├── game.py             # Console version
├── requirements.txt    # Dependencies
└── README.md          # Documentation
```

## Technologies

- **Python** - Core language
- **Streamlit** - Web framework
- **FontAwesome** - Icons

## License

MIT License
