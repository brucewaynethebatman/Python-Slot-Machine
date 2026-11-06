# 🎰 Python Slot Machine

A command-line slot machine game developed using **Python**. The application simulates a 3×3 slot machine where players can deposit funds, select betting lines, place bets, and earn payouts by matching symbols across horizontal rows.

Built to apply core Python programming concepts through a practical project.

## Overview

The game generates a grid of randomly selected symbols and evaluates the selected horizontal betting lines to determine winning combinations. It calculates payouts based on the number of winning lines and updates the player's remaining balance accordingly.

## Features

- **Balance Management** — Deposit an initial amount and track the remaining balance.
- **Flexible Betting** — Select between 1 and 3 betting lines.
- **Bet Validation** — Enforce minimum and maximum bet limits.
- **Randomized Gameplay** — Generate slot machine combinations using Python's `random` module.
- **Winning Detection** — Identify matching symbols across horizontal rows.
- **Automated Payouts** — Calculate winnings based on winning lines and the payout multiplier.
- **Input Validation** — Handle invalid entries and insufficient balances.

## Game Preview

<!-- Add your terminal screenshot here -->
<!-- Example: ![Slot Machine Preview](screenshots/game-preview.png) -->

## Game Rules

1. Make an initial deposit to start the game.
2. Select the number of betting lines (1–3).
3. Enter the amount to bet on each line.
4. The slot machine generates a 3×3 grid of random symbols.
5. A line wins when all three symbols in its horizontal row match.
6. Each winning line returns twice the amount bet on that line.

### Payout Calculation

**Total Bet**

`Bet Per Line × Number of Selected Lines`

**Total Winnings**

`Number of Winning Lines × Bet Per Line × Payout Multiplier`

**Final Balance**

`Initial Balance − Total Bet + Total Winnings`

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Random Module | Random symbol generation |
| VS Code | Development environment |

## Getting Started

### Prerequisites

- Python 3.8 or later
- Git (optional, for cloning the repository)

### Installation

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd YOUR_PROJECT_FOLDER
```

**3. Run the application**

```bash
python main.py
```

No third-party dependencies are required.

## Configuration

Game settings are managed through constants in the Python source code.

| Constant | Default Value | Description |
|---|---:|---|
| `ROWS` | 3 | Number of rows |
| `COLS` | 3 | Number of columns |
| `MAX_LINES` | 3 | Maximum betting lines |
| `MIN_BET` | 1 | Minimum bet per line |
| `MAX_BET` | 100 | Maximum bet per line |
| `PAYOUT_MULTIPLIER` | 2 | Winning payout multiplier |

## Python Concepts Demonstrated

This project applies the following programming concepts:

- Functions and modular programming
- Parameters, arguments, and return values
- Local and global scope
- Lists and nested lists
- Nested loops and iteration
- Conditional logic
- `break`, `continue`, and `for...else`
- Input validation and type conversion
- Random number generation
- Arithmetic operations and balance management

## Project Structure

```text
python-slot-machine/
│
├── main.py
└── README.md
```

## Future Improvements

Potential enhancements include:

- Multiple rounds of gameplay
- Customizable payout multipliers for different symbols
- Graphical user interface
- Game statistics and session history

## Author

**Lokesh Kumawat**
*Developed as a hands-on Python project to strengthen programming fundamentals and problem-solving skills.*
