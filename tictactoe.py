"""
Tic Tac Toe Player
"""
import copy
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
    if board is None:
        return {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                res.append((i,j))
    return set(res)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    play = player(board)
    act = list(actions(board))
    if not act.__contains__(action):
        raise ValueError

    res = copy.deepcopy(board)
    res[action[0]][action[1]] = play

    print(board)
    print(res)

    return res



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(0,len(board)):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    diag1 = board[0][0]
    diag1bool = True
    diag2 = board[0][2]
    diag2bool = True
    for i in range(0,len(board)):
        if diag1bool and board[i][i] != diag1:
            diag1bool = False
        if diag2bool and board[i][2-i] != diag2:
            diag2bool = False
    if diag1bool:
        return diag1
    if diag2bool:
        return diag2
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
    temp = []
    for i in range(len(acts)):

        num = recurser(result(board,acts[i]))
        temp.append((acts[i],num))

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
        play = player(board)
        loss = 0
        win = 0
        if play == "X":
            loss = -1
            win = 1
        else:
            loss = 1
            win = -1

        acts = list(actions(board))
        sum = 0
        for i in acts:
            res = result(board,i)
            if checkimmwin(res) == loss:
                return loss * 1000
            if checkimmwin(res) == win:
                return win * 1000
            sum += recurser(res)
        return sum

def checkimmwin(board):
    act = actions(board)
    for i in act:
        res = result(board,i)
        if res != 0:
           return res
    return 0
