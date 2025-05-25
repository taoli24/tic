board = [" "] * 9

print("Welcome to Tic Tac Toe!")
def print_board():
    print("Current board:")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    
def select_symbols():
    player1 = input("Player 1, choose your symbol (X or O): ").upper()
    while player1 not in ["X", "O"]:
        print("Invalid choice! Please choose X or O.")
        player1 = input("Player 1, choose your symbol (X or O): ").upper()
    
    return player1

def set_move(position, player):
    if board[position] == " ":
        board[position] = player
    else:
        print("Invalid move! Try again.")

def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)              # Diagonal
    ]
    
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None


def play_game():
    current_player = select_symbols()
    for _ in range(9):
        print_board()
        position = int(input(f"Player {current_player}, enter your move (1-9): "))
        
        set_move(position - 1, current_player)
        
        winner = check_winner()
        if winner:
            print_board()
            print(f"Player {winner} wins!")
            return
        
        current_player = "O" if current_player == "X" else "X"
    
    print_board()
    print("It's a draw!")
play_game()





