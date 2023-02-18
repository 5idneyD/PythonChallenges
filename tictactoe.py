

rows = {
    "A": 0,
    "B": 1,
    "C": 2
}


def print_board(cells):
    for i in range(3):
        print(" ___ ___ ___")
        print("| ", end="")
        for e in range(3):
            print(cells[e][i], end=" | ")
        print()
        print(" ___ ___ ___")


def newMove(cells, player):
    move = input("Choose cell (A1-C3): ")
    row = move[0].upper()
    col = int(move[1]) - 1
    row = rows[row]
    cells[col][row] = player
    return cells


def check_cols(cells, player):
    for i in range(3):
        if " " in set(cells[i]):
            pass
        elif len(set(cells[i])) == 1:
            print(player, " wins!")
            again = input("Play again y/n: ")
            if again.lower() == "y":
                game()
            else:
                print_board(cells)
                exit()


def check_rows(cells, player):
    for i in range(3):
        if " " in set([cells[0][i], cells[1][i], cells[2][i]]):
            pass
        elif len(set([cells[0][i], cells[1][i], cells[2][i]])) == 1:
            print(player, " wins!")
            again = input("Play again y/n: ")
            if again.lower() == "y":
                game()
            else:
                print_board(cells)
                exit()

def check_diagnol(cells, player):
    i = 0
    # print(set([cells[i][i], cells[i+1][i+1], cells[i+2][i+2]]))
    
    if len(set([cells[i][i], cells[i+1][i+1], cells[i+2][i+2]])) == 1:
        if " " in set([cells[i][i], cells[i+1][i+1], cells[i+2][i+2]]):
            pass
        else:
            print(player, " wins!")
            again = input("Play again y/n: ")
            if again.lower() == "y":
                game()
            else:
                print_board(cells)
                exit()
    elif len(set([cells[2][0], cells[1][1], cells[0][2]])) == 1:
        if " " in set([cells[2][0], cells[1][1], cells[0][2]]):
            pass
        else:
            print(player, " wins!")
            again = input("Play again y/n: ")
            if again.lower() == "y":
                game()
            else:
                print_board(cells)
                exit()        

def game():
    cells = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    print_board(cells)

    move = 1
    while True:
        if move % 2 == 0:
            player = "x"
        else:
            player = "o"

        newMove(cells, player)
        check_cols(cells, player)
        check_rows(cells, player)
        check_diagnol(cells, player)
        print_board(cells)
        move += 1
        
game()
