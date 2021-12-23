board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
active = "x"


def print_board(boar):
    for i in range(3):
        for j in range(3):
            print(boar[i][j], end=" ")
        print()


def check_draw(boar): 
    y = 0
    for i in range(3):
        for j in range(3):
            if boar[i][j] == '-':
                y = 1
    if y == 1:
        return False
    else:
        return True


def wierd_mark(boar, a, b, a_p):
    if no_problem(boar, a, b):
        boar[a][b] = a_p


def no_problem(boar, a, b):
    if boar[a][b] != "-":
        return False
    return True


def has_won(boar, a_p):
    for i in range(3):
        if boar[i][0] == boar[i][1] and boar[i][0] == boar[i][2] and boar[i][0] == a_p:
            return True
        if boar[0][i] == boar[1][i] and boar[0][i] == boar[2][i] and boar[0][i] == a_p:
            return True
    if boar[0][0] == boar[1][1] and boar[0][0] == boar[2][2] and boar[0][0] == a_p:
        return True
    if boar[2][0] == boar[1][1] and boar[2][0] == boar[0][2] and boar[2][0] == a_p:
        return True


def comp_move(boar, o):
    best_score = -1000
    best_move, best_mov = 0, 0

    for i in range(3):
        for j in range(3):
            if boar[i][j] == '-':
                boar[i][j] = o
                score = minimax(boar, False)
                boar[i][j] = '-'
                if score > best_score:
                    best_score = score
                    best_move, best_mov = i, j
    wierd_mark(boar, best_move, best_mov, o)


def minimax(boar, is_max):
    if has_won(boar, "o"):
        return 100
    elif has_won(boar, "x"):
        return -100
    elif check_draw(boar):
        return 0

    if is_max:
        best_score = -1000
        for i in range(3):
            for j in range(3):
                if boar[i][j] == '-':
                    boar[i][j] = "o"
                    score = minimax(boar, False)
                    boar[i][j] = '-'
                    if score > best_score:
                        best_score = score
        return best_score

    else:
        best_score = 1000
        for i in range(3):
            for j in range(3):
                if boar[i][j] == '-':
                    boar[i][j] = "x"
                    score = minimax(boar, True)
                    boar[i][j] = '-'
                    if score < best_score:
                        best_score = score
        return best_score


def main():
    global active
    if int(input("Do you want to go first or second [1/2]: ")) == 2:
        active = "o"
    while True:
        if check_draw(board):
            print("draw!")
            break

        if active == "x":
            x = int(input("Enter Pos (1-9): ")) - 1

            if no_problem(board, x // 3, x % 3):
                wierd_mark(board, x // 3, x % 3, active)
                print_board(board)
                if has_won(board, active):
                    print(f"\n{active} has won!")
                    break
                active = "o"

        elif active == "o":
            comp_move(board, active)
            print_board(board)
            if has_won(board, active):
                print(f"\n{active} has won!")
                break
            active = "x"
    if input("\n Wanna play again? [y/n]: ").lower() == "y":
        main()

if __name__ == '__main__':
    main()
