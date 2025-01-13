#!/usr/bin/python3

def print_board(board):
    """
    Prints the current game board.
    
    Parameters:
    board (list): The 3x3 grid representing the Tic Tac Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner on the board.
    
    Parameters:
    board (list): The 3x3 grid representing the Tic Tac Toe board.
    
    Returns:
    bool: True if there is a winner, False otherwise.
    """
    # Check rows for winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """
    Checks if the game is a draw (i.e., the board is full and there is no winner).
    
    Parameters:
    board (list): The 3x3 grid representing the Tic Tac Toe board.
    
    Returns:
    bool: True if the game is a draw, False otherwise.
    """
    for row in board:
        if " " in row:
            return False  # If there is any empty space, it's not a draw
    return True

def tic_tac_toe():
    """
    Main function that runs the Tic Tac Toe game, alternating turns between players.
    """
    board = [[" "]*3 for _ in range(3)]  # Initialize the 3x3 board
    player = "X"  # Player X starts the game

    while True:
        print_board(board)  # Print the current state of the board
        row = col = -1

        # Input validation for row and column
        while row not in [0, 1, 2]:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                if row not in [0, 1, 2]:
                    print("Invalid row! Please enter a value between 0 and 2.")
            except ValueError:
                print("Invalid input! Please enter an integer between 0 and 2.")

        while col not in [0, 1, 2]:
            try:
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if col not in [0, 1, 2]:
                    print("Invalid column! Please enter a value between 0 and 2.")
            except ValueError:
                print("Invalid input! Please enter an integer between 0 and 2.")
        
        # Check if the chosen spot is already taken
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
        else:
            # Place the player's mark on the board
            board[row][col] = player
            
            # Check if there's a winner
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            
            # Check for draw condition
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            
            # Switch player turn
            player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
