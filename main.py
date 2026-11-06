import random

# Define the dimensions of the slot machine grid.
ROWS = 3
COLS = 3

# Available symbols that can appear in the slot machine.
symbols = ["🍒", "🍋", "🍇", "🍊"]


def get_slot_machine_spin():
    # Store all columns of the slot machine.
    columns = []

    # Generate each column independently.
    for _ in range(COLS):
        column = []

        # Randomly select a symbol for each row in the current column.
        for _ in range(ROWS):
            symbol = random.choice(symbols)
            column.append(symbol)

        # Add the completed column to the main list.
        columns.append(column)

    # Return the complete 3x3 slot machine grid.
    return columns


def print_slot_machine(columns):
    # Iterate through row positions to display the grid horizontally.
    for row in range(ROWS):

        # Get the symbol at the current row from each column.
        for column in columns:
            print(column[row], end=" | ")

        # Move to the next line after printing all columns.
        print()


def check_winnings(columns, lines):
    # Store the row numbers where all three symbols match.
    winning_lines = []

    # Check only the number of rows selected by the player.
    for line in range(lines):

        # Use the first column's symbol as the reference for this row.
        symbol = columns[0][line]

        # Compare the same row across all columns.
        for column in columns:
            if column[line] != symbol:
                # Stop checking this row if any symbol doesn't match.
                break

        else:
            # The for-else block runs only if no mismatch was found.
            # Add 1 because players identify rows starting from 1, not 0.
            winning_lines.append(line + 1)

    # Return the list of winning row numbers.
    return winning_lines


def get_winnings(winning_lines, bet):
    # Calculate the payout based on winning rows and the bet per row.
    winnings = len(winning_lines) * bet * PAYOUT_MULTIPLIER
    return winnings


# Game configuration: limits and payout settings.
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
PAYOUT_MULTIPLIER = 2


def deposit():
    # Keep asking until the player enters a valid positive deposit.
    while True:
        amount = input("How much would you like to deposit? $")

        # Check whether the input contains only digits.
        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                print(f"Your balance ${amount} has been deposited.")
                break
            else:
                print("Amount must be greater than 0.")

        else:
            print("Please enter a number.")

    # Return the validated deposit amount.
    return amount


def get_number_of_lines():
    # Ask the player to select a valid number of betting lines.
    while True:
        lines = input(
            "Enter how many lines you want to bet on (1-"
            + str(MAX_LINES) + ")? "
        )

        if lines.isdigit():
            lines = int(lines)

            # Ensure the selected lines are within the allowed range.
            if 1 <= lines <= MAX_LINES:
                print(
                    f"You have selected {lines} "
                    f"{'line' if lines == 1 else 'lines'}."
                )
                break
            else:
                print("Please enter a valid number of lines.")

        else:
            print("Please enter a number.")

    # Return the validated number of lines.
    return lines


def get_bet(lines):
    # Ask the player for their bet on each selected line.
    while True:
        amount = input("What would you like to bet on each line? $")

        if amount.isdigit():
            amount = int(amount)

            # Check whether the bet is within the minimum and maximum limits.
            if MIN_BET <= amount <= MAX_BET:
                print(
                    f"You have selected ${amount} to bet on {lines} "
                    f"{'line' if lines == 1 else 'lines'}."
                )
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")

        else:
            print("Please enter a number.")

    # Return the validated bet amount per line.
    return amount


def main():
    # Display the game title.
    print("=" * 35)
    print("       🎰 SLOT MACHINE 🎰")
    print("=" * 35)

    # Collect the player's initial balance and betting preferences.
    balance = deposit()
    lines = get_number_of_lines()

    # Get the bet amount and calculate the total amount being wagered.
    bet = get_bet(lines)
    total_bet = bet * lines

    # Prevent the player from betting more than their available balance.
    if total_bet > balance:
        print(
            f"Error: Your current balance ${balance} is insufficient "
            f"to place that bet on {lines} "
            f"{'line' if lines == 1 else 'lines'} at ${bet} per line."
        )
        print("Please decrease your bet or increase your deposit.")
        return

    # Deduct the total bet before generating the slot machine result.
    remaining_balance = balance - total_bet

    # Generate and display the random slot machine combination.
    columns = get_slot_machine_spin()
    print_slot_machine(columns)

    # Identify winning rows and calculate the corresponding payout.
    winning_lines = check_winnings(columns, lines)
    winnings = get_winnings(winning_lines, bet)

    # Add the winnings to the balance remaining after the bet.
    remaining_balance += winnings

    # Display the final game results.
    print("=" * 35)
    print("          GAME RESULTS")
    print("=" * 35)

    print(f"Bet per line: ${bet}")
    print(f"Lines selected: {lines}")
    print(f"Total bet: ${total_bet}")

    # Display a different message depending on whether the player won.
    if winning_lines:
        print(f"Congratulations! You won on line(s): {winning_lines}")
    else:
        print("Sorry! No winning lines this time.")

    print(f"Total winnings: ${winnings}")
    print(f"Final balance: ${remaining_balance}")

    print("=" * 35)


# Start the game.
main()