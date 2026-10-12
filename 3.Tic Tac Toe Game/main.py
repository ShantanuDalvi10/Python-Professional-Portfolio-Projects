board = [" " for _ in range(9)]

def display_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("+---+---+-")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("+---+---+-")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(player):
    winnning_combinations = [
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6)
    ]

    for combination in winnning_combinations:
        if all(board[position] == player for position in combination):
            return True

    return False

def play_game():
    current_player = "X"
    print("Welcome to Tic Tac Toe Game")
    print("Choose positions from 1 to 9 ")
    print("Board positions are: ")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    display_board()

    while True:
        try:
            position = int(input(f"for {current_player}, Enter the number of position : "))

            if position < 1 and position > 9:
                print("Enter the number between 0 and 9.")
                continue

            if board[position - 1] != " ":
                print("This position is already occupied try another position.")
                continue

            board[position - 1 ] =  current_player

            display_board()

            if check_winner(current_player):
                print(f"Congratulations {current_player} is the winner.")
                break

            if " " not in board:
                print("It's a draw")
                break

            current_player = "O" if current_player=="X" else "X"

        except ValueError:
            print("Invalid Input. Try entering numbers between 0 and 9.")

play_game()
