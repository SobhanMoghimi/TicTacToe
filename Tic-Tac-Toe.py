# tic tac toe using adverserial search

import random


# Global variables
X = "X"
O = "O"
EMPTY = '-'
MAX_DEPTH = 3

def initial_board():
    """
    Creates starting board for game.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def next_player(board):
    """
    Returns the player who has the next turn on a board. (X or O).
    X starts the game.
    """
    x_count = 0
    o_count = 0
    # Count number of X's and O's on board
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1
    """
    Return the player who has the next turn, by counting the number of X's and O's on the board.
    """
    if x_count > o_count:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions available.
    The output is a set of tuples (i, j) where i is the row and j is the column.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            # if cell is empty, add it to the set of actions
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions

def change_board(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    If the action is not valid, return exception.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    new_board = [[board[i][j] for j in range(3)] for i in range(3)]
    new_board[action[0]][action[1]] = next_player(board)
    return new_board    

def winner(board):
    """
    Returns the winner of the game, if there is one. (X or O)
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    return None

def is_game_finished(board):
    """
    Returns True if game is over, False otherwise.
    Checking if we have a winner or if there are no more empty cells. (Draw)
    """
    if winner(board) != None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    # Draw
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.(Adverserial search for AI)
    """
    if is_game_finished(board):
        return None
    if next_player(board) == X:
        return max_value(board, 0)[1]
    else:
        return min_value(board, 0)[1]

def max_value(board, depth):
    """
    Returns the maximum value of the board.
    Depth is the current depth of the tree.
    For the max player, we want to maximize the value.
    """
    if is_game_finished(board) or depth == MAX_DEPTH:
        return utility(board), None
    v = -2
    action = None
    # For each action, get the min value of the resulting board
    for a in actions(board):
        min_v = min_value(change_board(board, a), depth + 1)[0]
        # If the min value is greater than the current max value, update the max value
        if min_v > v:
            v = min_v
            action = a
    return v, action

def min_value(board, depth):
    """
    Returns the minimum value of the board.
    Depth is the current depth of the tree.
    For the min player, we want to minimize the value.
    """
    if is_game_finished(board) or depth == MAX_DEPTH:
        return utility(board), None
    v = 2
    action = None
    # For each action, get the max value of the resulting board
    for a in actions(board):
        max_v = max_value(change_board(board, a), depth + 1)[0]
        # If the max value is less than the current min value, update the min value
        if max_v < v:
            v = max_v
            action = a
    return v, action

def print_board(board):
    """
    Prints the board in terminal.
    """
    for row in board:
        print(row)

def main():
    board = initial_board()
    # chose random player to start (AI or human)
    if random.randint(0, 1) == 0:
        player = True
    else:
        player = False
    # The First player is X
    if(player):
        print("AI starts")
        players_sign = O
    else:
        print("Human starts")
        players_sign = X
    # Game loop
    while not is_game_finished(board):
        # AI turn
        if player:
            print("AI's turn")
            # Get the optimal action
            board = change_board(board, minimax(board))
            print_board(board)
            print('\n')
        # Human turn
        else:
            print("Your turn")
            print("Enter row and column (0-2)")
            move = None
            # Geting valid move from human
            while move not in actions(board):
                row_move = int(input("Enter row: "))
                col_move = int(input("Enter column: "))
                move = (row_move, col_move)
            # Updating board
            board = change_board(board, move)
            print_board(board)
            print('\n')
        player = not player
    # Game is finished
    print("Game is finished!")
    # Check who won. If there is no winner, it's a draw.
    if winner(board) == players_sign:
        print("You win")
    elif winner(board) != players_sign and winner(board) != None:
        print("AI wins")
    else:
        print("Draw")

if __name__ == "__main__":
    main()