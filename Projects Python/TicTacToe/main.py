def print_board(board_values):
    board = f"| {board_values[0]} | {board_values[1]} | {board_values[2]} | \n" \
            f"| {board_values[3]} | {board_values[4]} | {board_values[5]} | \n" \
            f"| {board_values[6]} | {board_values[7]} | {board_values[8]} |"
    return board


def player1(moves_p1):
    posMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    badMoves = ['X', 'O']

    try:
        pos = int(input(f"Your move ({posMoves}):  ".replace("[", "").replace(']', "")))
        print("")

        while pos not in posMoves or moves_p1[pos - 1] in badMoves:
            pos = int(input(f"The position is taken or is not a correct move ({posMoves}): "))
            print("")
    except ValueError:
        print("\nWrong Input!\n")

    moves_p1[pos - 1] = 'X'
    return moves_p1


def player2(moves_p2):
    posMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    badMoves = ['X', 'O']
    try:
        pos = int(input(f"Your move ({posMoves}):  ".replace("[", "").replace(']', "")))

        while pos not in posMoves or moves_p2[pos - 1] in badMoves:
            pos = int(input(f"The position is taken or is not a correct move ({posMoves}): "))
            print("")
    except ValueError:
        print("\nWrong Input!\n")

    moves_p2[pos - 1] = 'O'
    return moves_p2


def check_win(win_moves):
    for i in range(0, 7, 3):
        print(i)
        if win_moves[i] == win_moves[i + 1] == win_moves[i + 2] != "-":
            return win_moves[i]
    for i in range(3):
        if win_moves[i] == win_moves[i + 3] == win_moves[i + 6] != "-":
            return win_moves[i]
    if win_moves[0] == win_moves[4] == win_moves[8] != "-":
        return win_moves[0]
    if win_moves[2] == win_moves[4] == win_moves[6] != "-":
        return win_moves[2]
    return "None"


def game(in_game_moves):
    turn = "X"
    while "-" in in_game_moves:
        print(f"Is {turn} turn!")
        print("")
        if turn == "X":
            turn = "O"
            print("")
            print(print_board(player1(in_game_moves)))
            print("")
        else:
            turn = "X"
            print(print_board(player2(in_game_moves)))
            print("")
        if check_win(in_game_moves) != "None":
            return f'{check_win(in_game_moves)} wins!'
    return "Draw!"


if __name__ == '__main__':

    playPos = input("Press any button to play \nPress 2 to exit")

    while playPos != "2":
        moves = ["-"] * 9
        print(print_board(moves))
        print(game(moves))
        playPos = int(input("\nInsert any number to play again \nPress 2 to exit\n"))

    print("Have a nice day!")
