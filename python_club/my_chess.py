# print("╔╠╦╗╣╬╝═╞╟╡╢╪╫╨╥╧╤║╩╚")
s = [["  ", "  ", "  ", "  ", "  "],
     ["  ", "  ", "  ", "  ", "  "],
     ["  ", "  ", "  ", "  ", "  "],
     ["  ", "  ", "  ", "  ", "  "],
     ["  ", "  ", "  ", "  ", "  "]]
turn = -1


def chess(a, b):
    global s
    global turn
    if s[a - 1][b - 1] != "  ":
        print('DO NOT CHEAT!')
        return
    if turn == -1:
        s[a - 1][b - 1] = "X "
    else:
        s[a - 1][b - 1] = "O "
    turn = -turn
    print("╔══╦══╦══╦══╦══╗")
    print("║%s║%s║%s║%s║%s║" % tuple(s[0]))
    print("╠══╬══╬══╬══╬══╣")
    print("║%s║%s║%s║%s║%s║" % tuple(s[1]))
    print("╠══╬══╬══╬══╬══╣")
    print("║%s║%s║%s║%s║%s║" % tuple(s[2]))
    print("╠══╬══╬══╬══╬══╣")
    print("║%s║%s║%s║%s║%s║" % tuple(s[3]))
    print("╠══╬══╬══╬══╬══╣")
    print("║%s║%s║%s║%s║%s║" % tuple(s[4]))
    print("╚══╩══╩══╩══╩══╝")

    # print(type(s[a-1][b-1]))
    # print(s[b-1][a-1:a+2])
    # print(s[a-1][b-1])


#
    # TODO 横排判断：Done

    for i in range(0, 5):
        for j in range(0, 5):
            if s[i][j:j+3] == ['X ', 'X ', 'X ']:
                print("X wins!")
            elif s[i][j:j+3] == ['O ', 'O ', 'O ']:
                print("O wins!")

    # TODO 竖排判断：Done

    for j in range(0, 5):
        for i in range(0, 3):
            if s[i][j] == s[i+1][j] == s[i+2][j] == 'X ':
                print("X wins!")
            elif s[i][j] == s[i+1][j] == s[i+2][j] == 'O ':
                print("O wins!")

    # TODO 斜排判断：Done

    for i in range(0, 3):
        for j in range(0, 3):
            if s[i][j] == s[i+1][j+1] == s[i+2][j+2] == 'X ':
                print("X wins!")
            elif s[i][j] == s[i+1][j+1] == s[i+2][j+2] == 'O ':
                print("O wins!")

    for j in range(2, 5):
        for i in range(0, 3):
            if s[i][j] == s[i+1][j-1] == s[i+2][j-2] == 'X ':
                print("X wins!")
            elif s[i][j] == s[i+1][j-1] == s[i+2][j-2] == 'O ':
                print("O wins!")


while True:
    a = input("row：")
    b = input("rank：")

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Please enter: ")
        continue
    if a not in range(0, 6) or b not in range(0, 6):
        print("Illegal! ")
        continue
    chess(a, b)
