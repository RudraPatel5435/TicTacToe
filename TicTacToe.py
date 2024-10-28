game = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
player2 = 0
player1 = 0
playing = True
choosing = True

while choosing:
    player1 = input("Player 1, choose your marker (X or O): ").strip().upper()
    if player1 == "X":
        player2 = "O"
        choosing=False
    elif player1 == "O":
        player2 ="X"
        choosing = False
    else:
        print("Enter valid choice.")

print("Player 1 (" + player1 + ") - Player 2 (" + player2 + ")")

def layout():
    print("     |     |     ")
    print("  " + str(game[0][0]) + "  |  " + str(game[0][1]) + "  |  " + str(game[0][2]) + "  ")
    print("     |     |     ")
    print("-----|-----|-----")
    print("     |     |     ")
    print("  " + str(game[1][0]) + "  |  " + str(game[1][1]) + "  |  " + str(game[1][2]) + "  ")
    print("     |     |     ")
    print("-----|-----|-----")
    print("     |     |     ")
    print("  " + str(game[2][0]) + "  |  " + str(game[2][1]) + "  |  " + str(game[2][2]) + "  ")
    print("     |     |     ")
layout()

while playing:
    choice1 = input("It's player 1's turn. Enter your slot: ")
    print("Player 1 (X) - Player 2 (O)")
    for i in range(0,3):
        for j in range(0,3):
            if choice1 == game[i][j]:
                game[i][j] = player1
    layout()
    if (game[0].count("X") == 3) or (game[1].count("X") == 3) or (game[2].count("X") == 3) or (game[0][0]=="X" and game[1][0]=="X" and game[2][0]=="X") or (game[0][1]=="X" and game[1][1]=="X" and game[2][1]=="X") or (game[0][0]=="X" and game[1][1]=="X" and game[2][2]=="X") or (game[0][2]=="X" and game[1][1]=="X" and game[2][0]=="X"):
        if player1 == "X":
            print("Player 1 (" + player1 + ") Won!")
        break
    if (game[0].count("O") == 3) or (game[1].count("O") == 3) or (game[2].count("O") == 3) or (game[0][0]=="O" and game[1][0]=="O" and game[2][0]=="O") or (game[0][1]=="O" and game[1][1]=="O" and game[2][1]=="O") or (game[0][0]=="O" and game[1][1]=="O" and game[2][2]=="O") or (game[0][2]=="O" and game[1][1]=="O" and game[2][0]=="O"):
        if player1 == "O":
            print("Player 1 (" + player1 + ") Won!")
        break
    check = 0
    for a in game:
        for b in a:
            if b == "O" or b == "X":
                check+=1
    if check == 9:
        print("Draw!")
        break

    choice2 = input("It's player 1's turn. Enter your slot: ")
    print("Player 1 (X) - Player 2 (O)")
    for k in range(0, 3):
        for h in range(0, 3):
            if choice2 == game[k][h]:
                game[k][h] = player2
    layout()
    if (game[0].count("X") == 3) or (game[1].count("X") == 3) or (game[2].count("X") == 3) or (game[0][0]=="X" and game[1][0]=="X" and game[2][0]=="X") or (game[0][1]=="X" and game[1][1]=="X" and game[2][1]=="X") or (game[0][0]=="X" and game[1][1]=="X" and game[2][2]=="X") or (game[0][2]=="X" and game[1][1]=="X" and game[2][0]=="X"):
        print("Player 2 (" + player2 + ") Won!")
        break
    if (game[0].count("O") == 3) or (game[1].count("O") == 3) or (game[2].count("O") == 3) or (game[0][0]=="O" and game[1][0]=="O" and game[2][0]=="O") or (game[0][1]=="O" and game[1][1]=="O" and game[2][1]=="O") or (game[0][0]=="O" and game[1][1]=="O" and game[2][2]=="O") or (game[0][2]=="O" and game[1][1]=="O" and game[2][0]=="O"):
        print("Player 2 (" + player2 + ") Won!")
        break
    check = 0
    for a in game:
        for b in a:
            if b == "O" or b == "X":
                check+=1
    if check == 9:
        print("Draw!")
        break
