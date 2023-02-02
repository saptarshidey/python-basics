import random

MAX_LINES = 4
MAX_BET = 100
ROWS = 4
COLS = 3

symbol_count = { "A": 1, "B": 2, "C": 3, "D": 4 }
symbol_value = { "A": 5, "B": 4, "C": 3, "D": 2 }

def deposit():
    is_valid_input = False
    while not is_valid_input:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0: is_valid_input = True

        if not is_valid_input: print("Please enter a valid positive number")

    return amount

def get_lines():
    is_valid_input = False
    while not is_valid_input:
        lines = input(f"Enter the number of lines to bet on (1 - {MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <= MAX_LINES: is_valid_input = True

        if not is_valid_input: print("Please enter a valid positive number")

    return lines

def get_bet():
    is_valid_input = False
    while not is_valid_input:
        bet = input(f"What would you like to bet on each line($1 - ${MAX_BET})? $")
        if bet.isdigit():
            bet = int(bet)
            if bet >= 1 and bet <= MAX_BET: is_valid_input = True

        if not is_valid_input: print("Please enter a valid positive number")

    return bet

def play(balance):
    lines = get_lines()
    is_valid_bet = False

    while not is_valid_bet:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            is_valid_bet = True
        else:
            print(f"You do not have enough balance to bet that amount. Your current balance is ${balance}")

    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}")
    spin_result = spin(ROWS, COLS, symbol_count)
    win, winning_lines = calc_win(spin_result, lines, bet, symbol_value)
    print_slot_machine(spin_result)

    print(f"You won ${win}")
    print(f"You won on lines: {winning_lines}")

    return win - total_bet

def spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            val = random.choice(current_symbols)
            column.append(val)
            current_symbols.remove(val)

        columns.append(column)

    return columns

def print_slot_machine(spin_result):
    for row in range(ROWS):
        for col in range(COLS):
            if col == 0: print(' | ', end = '')
            print(spin_result[col][row], end = ' | ')
        print()

def calc_win(spin_result, lines, bet, values):
    win = 0
    winning_lines = []

    for row in range(lines):
        symbol = spin_result[0][row]
        for col in range(1, COLS):
            if spin_result[col][row] != symbol: break
        else:
            win = win + values[symbol] * bet
            winning_lines.append(row + 1)

    return win, winning_lines

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        inp = input("Press any key to play (q to quit): ")
        if inp.lower() == 'q': break
        win_or_loss = play(balance)
        balance = balance + win_or_loss

main()
