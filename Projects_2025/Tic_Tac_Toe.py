board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

game_running = True
current_player = "X"

def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def handle_turn():
    global current_player
    print(f"{current_player}'s turn")

    position = input("Choose a position between 1-9: ")

    valid = False
    while not valid:
        # Make sure the player inputs a valid position
        while position not in ['1','2','3','4','5','6','7','8','9']:
            position = input("Choose a position between 1-9: ")
        # Convert to integer and adjust to match board array (0-8)
        position = int(position) - 1

        if board[position] == ' ':
            valid = True
        else:
            print("This spot is already taken, please choose another.")
            position = input("Choose a position between 1-9: ")
            continue

        board[position] = current_player

        display_board()

def check_for_winner():
    global game_running, current_player

    # Check rows
    row_1 = board[0] == board[1] == board[2] != ' '
    row_2 = board[3] == board[4] == board[5] != ' '
    row_3 = board[6] == board[7] == board[8] != ' '

    # Check columns
    col_1 = board[0] == board[3] == board[6] != ' '
    col_2 = board[1] == board[4] == board[7] != ' '
    col_3 = board[2] == board[5] == board[8] != ' '

    diagonal_1 = board[0] == board[4] == board[8] != ' '
    diagonal_2 = board[6] == board[4] == board[2] != ' '

    if row_1 or row_2 or row_3 or col_1 or col_2 or col_3 or diagonal_1 or diagonal_2:
        game_running = False
        print(f"{current_player} wins!")

def check_for_tie():
    global game_running

    if " " not in board:
        game_running = False
        print("It's a tie!")

def check_if_game_over():
    check_for_winner()
    check_for_tie()

def swap_player():
    global current_player

    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'


def play_game():
    global game_running

    print("\nWelcome to Tic Tac Toe!")
    print("The board positions are numbered like this:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print("\nStarting game with empty board:")
    display_board()

    while game_running == True:
        print("Game running")
        # handle single turn
        handle_turn()

        # check for win
        check_if_game_over()

        # swap player
        swap_player()

    print("Thanks for playing!")

play_game()