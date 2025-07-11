# Implement a tic tac toe command line game  with a Min Max AI (if you feel like it)
import numpy as np

board = np.zeros((3, 3))

show_board = np.empty((3, 3), str)
show_board[:] = ' '


def make_play(play, player_mark, game):
    if play > 10:
        return False
    a, b = convert_play(play)
    value = game[a][b]
    if value == 0:
        game[a][b] = 1 if player_mark == 'X' else 2
        show_board[a][b] = player_mark
        return True
    return False


def display_board():
    for i in range(0, 3):
        print(f" {show_board[i][0]}|{show_board[i][1]}|{show_board[i][2]}")
        if i != 2:
            print("--------")


def convert_play(play):
    if play == 1:
        return 0, 0
    elif play == 2:
        return 0, 1
    elif play == 3:
        return 0, 2
    elif play == 4:
        return 1, 0
    elif play == 5:
        return 1, 1
    elif play == 6:
        return 1, 2
    elif play == 7:
        return 2, 0
    elif play == 8:
        return 2, 1
    elif play == 9:
        return 2, 2


def reconvert_play(play):
    if play == (0, 0):
        return 1
    elif play == (0, 1):
        return 2
    elif play == (0, 2):
        return 3
    elif play == (1, 0):
        return 4
    elif play == (1, 1):
        return 5
    elif play == (1, 2):
        return 6
    elif play == (2, 0):
        return 7
    elif play == (2, 1):
        return 8
    elif play == (2, 2):
        return 9


def player_turn(player_mark, game):
    player_message = 'Player 1 turn' if player_mark == 'X' else 'Player 2 turn'
    valid_play = False
    while valid_play is False:
        try:
            play = int(input(player_message))
            valid_play = make_play(play, player_mark, game)
            if valid_play is False:
                print('Impossible play')
            else:
                return True
        except:
            print('Inform a number between 1 and 9')


def check_winner(player_value, game):
    if check_horizontals(player_value, game):
        return True
    elif check_verticals(player_value, game):
        return True
    elif check_diagonals(player_value, game):
        return True
    else:
        return False


def check_horizontals(player_value, game):
    for z in range(0, 3):
        score = 0
        for i in range(0, 3):
            if game[z, i] == player_value:
                score += 1
        if score == 3:
            return True

    return False


def check_verticals(player_value, game):
    for z in range(0, 3):
        score = 0
        for i in range(0, 3):
            if game[i, z] == player_value:
                score += 1
        if score == 3:
            return True

    return False


def check_diagonals(player_value, game):
    score = 0
    for z in range(0, 3):
        if game[z, z] == player_value:
            score += 1
    if score == 3:
        return True
    score = 0
    z = 2
    for i in range(0, 3):
        if game[z, i] == player_value:
            score += 1
        z = z - 1
    if score == 3:
        return True

    return False


def get_utility(player, game):

    max_player = 1
    min_player = 2
    if player % 2 == 0:
        max_player = 2
        min_player = 1
    if check_diagonals(max_player, game):
        return 9999
    elif check_diagonals(min_player, game):
        return -9999
    elif check_horizontals(max_player, game):
        return 9999
    elif check_horizontals(min_player, game):
        return -9999
    elif check_verticals(max_player, game):
        return 9999
    elif check_verticals(min_player, game):
        return -9999
    else:
        return 0


def is_terminal(game):
    value = get_utility(1, game)
    if (0 in board) is False:
        return True
    if value == 9999 or value == -9999 or 0 not in game:
        return True
    return False


def get_possible_actions(game):
    a = []
    for i in range(0, 3):
        for z in range(0, 3):
            if game[i][z] == 0:
                a.append((i, z))

    return a
def search_minmax(game, state):
    game_copy = np.copy(board)
    value, move = max_value(game_copy, -9999, +9999)
    return move


def max_value(game, alfa, beta):
    if is_terminal(game):
        return get_utility(1, game), None

    v = -9999
    for a in get_possible_actions(game):
        game[a[0], a[1]] = 1
        v2, a2 = min_value(game, alfa, beta)
        if v2 > v:
            v, move = v2, a
            alfa = max(alfa, v)
        if v >= beta:
            return v, a
    return v, None


def min_value(game, alfa, beta):
    if is_terminal(game):
        return get_utility(1, game), None

    v = 9999
    for a in get_possible_actions(game):
        game[a[0], a[1]] = 2
        v2, a2 = max_value(game, alfa, beta)
        if v2 < v:
            v, move = v2, a
            beta = min(beta, v)
        if v <= alfa:
            return v, a
    return v, None


def begin_game():
    game_variable = False
    while True:

        play = search_minmax(board, None)
        converted_play = reconvert_play(play)
        make_play(converted_play,'X', board)
        display_board()
        if check_winner(1, board):
            print('Player 1 wins!')
            break
        if (0 in board) is False:
            print('Draw!')
            break
        player_turn('O', board)
        display_board()
        if check_winner(2, board):
            print('Player 2 wins!')
            break
        if (0 in board) is False:
            print('Draw!')
            break


begin_game()

