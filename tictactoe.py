"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0

    for i in board:
        for j in i:
            if j == EMPTY:
                count += 1

    if count % 2 == 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res = []

    if not terminal(board):
        for i in range(len(board)):
            for j in range(i):
                if board[i][j] == EMPTY:
                    res.append((i,j))
        return set(res)
    else:
        return {}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    play = player(board)
    if not actions(board).__contains__(action):
        raise ValueError
    res = board.copy()[action[0]][action[1]] = play

    return res



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in board:
        winnerel = True
        comp = i[0]
        for j in i:
            if j != comp:
                winnerel = False
                break
        if winnerel:
            return comp

    winner1 = False
    comp1 = board[0][0]
    winner2 = False
    comp2 = board[0][2]

    for i in range(3):
        winnerel = True
        comp = board[0][i]
        for j in range(3):
            if board[j][i] != comp:
                winnerel = False
                break
        if winnerel:
            return comp

        if winner1 and board[i][i] != comp1:
            winner1 = False
        if winner2 and board[i][2-i] != comp2:
            winner2 = False

    if winner1:
        return comp1
    elif winner2:
        return comp2
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True
    if len(actions(board)) == 0:
        return True
    else:
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    match win:
        case "X":
            return 1
        case "O":
            return -1
        case _:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    play = player(board)

    acts = list(actions(board))
    print(acts)
    temp = []
    for i in range(len(acts)):
        num = recurser(result(board,acts[i]))
        temp.append((acts[i],num))
    print(temp)

    if temp:
        select = temp[0][1]
        selectact = temp[0][0]
        if play == "X":
            for i in range(1,len(temp)):
                if temp[i][1] > select:
                    select = temp[i][1]
                    selectact = temp[i][0]
            return selectact
        else:
            for i in range(1,len(temp)):
                if temp[i][1] < select:
                    select = temp[i][1]
                    selectact = temp[i][0]
            return selectact
    else:
        return None


def recurser(board):
    if terminal(board):
        return utility(board)
    else:
        acts = list(actions(board))
        sum = 0
        for i in acts:
            sum += recurser(result(board,i))
        return sum

