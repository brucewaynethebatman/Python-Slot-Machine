# 🎰 Python Slot Machine Game

A command-line Slot Machine game built using Python. The game allows players to deposit money, select betting lines, place bets, and try their luck with randomly generated slot combinations.

The game continues running until the player decides to exit, allowing multiple rounds without restarting the program.

## 🚀 Features

- **Random Slot Generation:** Uses Python's `random` module to generate a 3×3 slot machine grid.
- **Deposit System:** Players can deposit an initial balance.
- **Flexible Betting:** Choose between 1 and 3 betting lines.
- **Bet Validation:** Enforces minimum and maximum betting limits.
- **Winning Detection:** Checks whether all three symbols match across a selected row.
- **Payout System:** Calculates winnings using a predefined payout multiplier.
- **Balance Management:** Deducts bets and adds winnings to the remaining balance.
- **Continuous Gameplay:** Uses `while True` to keep the game running until the player chooses to exit.
- **Replay Option:** Players can start another round without restarting the program.
- **Input Validation:** Handles invalid inputs and prevents incorrect betting values.

## 🛠️ Technologies Used

- Python
- Random Module
- Loops (`for`, `while`)
- Conditional Statements (`if`, `else`, `break`)
- Functions
- Lists and Nested Lists
- User Input Handling
- Basic Game Logic

## 🎮 How to Play

1. Run the Python program.
2. Enter your initial deposit.
3. Select the number of betting lines (1–3).
4. Enter your bet amount per line.
5. The slot machine generates a random 3×3 combination.
6. If all three symbols match on a selected row, you win.
7. Your winnings are calculated and added to your remaining balance.
8. Choose whether to play another round or exit.

## 📋 Game Configuration

| Setting | Value |
|---|---|
| Grid Size | 3 × 3 |
| Available Symbols | 🍒 🍋 🍇 🍊 |
| Minimum Bet | $1 |
| Maximum Bet | $100 |
| Maximum Betting Lines | 3 |
| Payout Multiplier | 2x |

## 💻 Installation & Execution

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd slot-machine
```

**3. Run the game**

```bash
python main.py
```

No external packages are required. The game uses Python's built-in `random` module.

## 📚 What I Learned

Through this project, I practiced:

- Implementing infinite loops using `while True`.
- Using `break` to control loop termination.
- Validating user input before processing it.
- Working with nested lists and loops.
- Breaking a larger program into reusable functions.
- Implementing randomization and conditional game logic.
- Managing balances and calculating payouts.
- Building a continuous command-line application.

## 🔮 Future Improvements

- Add a persistent balance system across multiple rounds.
- Introduce multiple winning patterns.
- Add different symbols with different payout values.
- Improve the game interface with a more interactive design.
- Add automated tests for game logic and payout calculations.

---

**Author:** Lokesh Kumawat

*Built as a Python practice project to strengthen programming fundamentals and problem-solving skills.*
