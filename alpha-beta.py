import os
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def print_board(board): # prints the board
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=' ')
        print()

def no_problem(board, a, b):    # checks if the suggested position of the board is taken
    if board[a][b] != '-':
        return False
    return True

def is_full(board): # checks if board is full
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '-':
                return False
    return True

def mark_board(board, a, b, active):    # marks the board
    board[a][b] = active

def has_won(board, active): # checks if has won
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] == active:
            return True
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] == active:
            return True
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == active:
        return True
    if board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[2][0] == active:
        return True 

def comp_move(board):
    best_score = -1000
    best_mov, best_move = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'o'
                score = minimax(board, -1000, 1000, False)
                board[i][j] = '-'
                if score > best_score:
                    best_score = score
                    best_mov, best_move = i, j
    mark_board(board, best_mov, best_move, 'o')

def minimax(board, alpha, beta, is_max):
    if has_won(board, 'o'):
        return 100
    elif has_won(board, 'x'):
        return -100
    elif is_full(board):
        return 0
    if is_max:
        best_score = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'o'
                    score = minimax(board, alpha, beta, False)
                    board[i][j] = '-'
                    if score > best_score:
                        best_score = score
                        if alpha < best_score:
                            alpha = best_score
                        if best_score >= beta:
                            break
        return best_score
   
    if not is_max:
        best_score = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'x'
                    score = minimax(board, alpha, beta, True)
                    board[i][j] = '-'
                    if score < best_score:
                        best_score = score
                        if beta > best_score:
                            beta = best_score
                        if best_score <= alpha:
                            break
        return best_score

def main(active = 'x'):
    if input('Do you want to go first? (y/n): ').lower() == 'n':
        active = 'o'

    while not is_full(board):
        if active == 'x':
            place = int(input('enter a number [1-9]: ')) - 1
            if no_problem(board, place // 3, place % 3):
                mark_board(board, place // 3, place % 3, active)
                os.system('cls')
                print_board(board)
                if has_won(board, active):
                    print(f"{active} won!")
                    break
                active = 'o'
        if active == 'o':
            comp_move(board)
            os.system('cls')
            print_board(board)
            if has_won(board, active):
                print(f"{active} won!")
                break
            active = 'x'
    if is_full(board):
        print("draw!")
    if input('do you want to play again [y/n]: ').lower() == 'y':
        main()
main()