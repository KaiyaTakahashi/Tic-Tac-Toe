"""
Tic Tac Toe

Students:
Guilherme de Almeida
Kaiya Takahashi
"""

import random

type_p1 = "X"
type_p2 = "O"


class RangeError(Exception):
    pass


class PosTaken(Exception):
    pass


def print_board():
    """
    Print the boeard (#) for the list l[][]
    """
    print("\n   Game                  Positions")
    aux = 0
    for i in range(3):
        print(f" {l[i][0]} | {l[i][1]} | {l[i][2]}       |       {aux + 1 } | {aux + 2} | {aux + 3}")
        aux += 3
        if i < 2:
            print("---|---|---      |      ---|---|---")
    print()


def check_win(alist) -> bool:
    """
    Check if there's a winner for the list (alist) and returns a boolean value
    :param alist: the list to be checked
    :return: true if there`s a winner / false for no winner
    """
    if (alist[0][0] == alist[1][0] == alist[2][0] and alist[0][0] != " ") or (alist[0][1] == alist[1][1] == alist[2][1] and alist[0][1] != " ") or (alist[0][2] == alist[1][2] == alist[2][2] and alist[0][2] != " ") or (alist[0][0] == alist[0][1] == alist[0][2] and alist[0][0] != " ") or (alist[1][0] == alist[1][1] == alist[1][2] and alist[1][0] != " ") or (alist[2][0] == alist[2][1] == alist[2][2] and alist[2][0] != " ") or (alist[0][0] == alist[1][1] == alist[2][2] and alist[0][0] != " ") or (alist[0][2] == alist[1][1] == alist[2][0]  and alist[0][2] != " "):
        return True
    return False


def insert_position(player) -> bool:
    """
    Ask the user the number of field to play, validates it and returns a boolean based on the check_win function
    :param player: which player is playing? (1 or 2)
    :return: true or false / based on the check_win function
    """
    count = 0
    pos = 0
    print_board()
    pos_check = False
    while not pos_check:
        try:
            pos = int(input(f"Player {player}, choose a position: "))
            if not (0 < pos < 10):
                raise RangeError
            pos -= 1
            posY = pos // 3
            posX = pos % 3
            if l[posY][posX] != " ":
                raise PosTaken
            if player == 1:
                l[posY][posX] = type_p1
            else:
                l[posY][posX] = type_p2
            count += 1
            pos_check = True
            return check_win(l)
        except ValueError:
            print("Invalid value!")
        except RangeError:
            print("Invalid range value. Please choose a number between 1 and 9.")
        except PosTaken:
            print(f"Position {pos + 1} already taken!")


def insert_position_ai(player):
    """
    AI function to choose a position on the board
    :param player: the number of the player (2)
    :return: true or false / based on the check_win function
    """
    # check all positions if it's possible to win with one move
    count = 0
    for row in range(0, len(l)):
        for col in range(0, len(l[row])):
            count += 1
            copyList = [row2[:] for row2 in l]
            if l[row][col] == " ":
                copyList[row][col] = type_p2
                if check_win(copyList): # check if AI can win
                    l[row][col] = type_p2
                    print(f"Player {player}, choose a position: {count}")
                    return check_win(l)
    # check all position if it's possible to lose with one position (then block)
    count = 0
    for row in range(0, len(l)):
        for col in range(0, len(l[row])):
            count += 1
            copyList = [row2[:] for row2 in l]
            if l[row][col] == " ":
                copyList[row][col] = type_p1
                if check_win(copyList): # check if player can win
                    l[row][col] = type_p2
                    print(f"Player {player}, choose a position: {count}")
                    return check_win(l)
    # if the center position is blank then check there
    if l[1][1] == " ":
        l[1][1] = type_p2
        print(f"Player {player}, choose a position: 5")
        return check_win(l)

    # Check if the computer can win on the next next step
    for i in range(0, 9):
        row = i // 3
        col = i % 3
        if l[row][col] == " ":
            for j in range(i + 1, 9):
                row2 = j // 3
                col2 = j % 3
                if l[row2][col2] == " ":
                    copyList = [row2[:] for row2 in l]  # to copy the list
                    copyList[row][col] = type_p2
                    copyList[row2][col2] = type_p2
                    if check_win(copyList):  # check if player can win
                        l[row2][col2] = type_p2
                        print(f"Player {player}, choose a position: {j + 1}")
                        return check_win(l)

    # randon position / no winner
    while True:
        col = random.randint(0, 2)
        row = random.randint(0, 2)
        if l[row][col] == " ":
            count = (row * 3) + col + 1
            l[row][col] = type_p2
            print(f"Player {player}, choose a position: {count}")
            return check_win(l)


def mode_two_players():
    """
    Controls the game for 2 players
    """
    count = 0
    while count < 9:
        if insert_position(1):
            print_board()
            print("Player 1 Wins!")
            break
        count += 1
        if count > 8:
            print_board()
            print("Draw!")
            break
        if insert_position(2):
            print_board()
            print("PLayer 2 Wins!")
            break
        count += 1


def mode_one_player():
    """
    Controls the game for 1 player vs AI
    """
    count = 0
    while count < 9:
        if insert_position(1):
            print_board()
            print("Player 1 Wins!")
            break
        count += 1
        if count > 8:
            print_board()
            print("Draw!")
            break
        if insert_position_ai(2):
            print_board()
            print("AI (computer) Wins!")
            break
        count += 1


opt = 0
while opt != 3:  # keeps the game running until the user choose the quit option
    l = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print("==== TIC TAC TOE ====\n")
    print("1. Two-player game (Player 1 vs Player 2)")
    print("2. Player vs AI (computer)")
    print("3. Quit Game")
    print()
    while not 0 < opt < 4:
        try:
            opt = int(input("Select Game Mode: "))
            if not 0 < opt < 4:
                raise RangeError
        except ValueError:
            print("Invalid Value")
            opt = 0
        except RangeError:
            print("Invalid option!")
    if opt == 1:
        mode_two_players()
    elif opt == 2:
        mode_one_player()
    else:
        break
    input("\nPress 'enter' to continue...")
    opt = 0
