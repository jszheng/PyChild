s = [["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
     ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]]
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
    print("╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗")
    print("║%s║%s║%s║%s║%s║%s║%s║%s║%s║%s║" % tuple(s[0]))
    print("╠══╬══╬══╬══╬══╬══╬══╬══╬══╬══╣")
    print("║%s║%s║%s║%s║%s║%s║%s║%s║%s║%s║" % tuple(s[1]))
    print("╠══╬══╬══╬══╬══╬══╬══╬══╬══╬══╣")
    print("║%s║%s║%s║%s║%s║%s║%s║%s║%s║%s║" % tuple(s[2]))
    print("╠══╬══╬══╬══╬══╬══╬══╬══╬══╬══╣")
    print("║%s║%s║%s║%s║%s║%s║%s║%s║%s║%s║" % tuple(s[3]))
    print("╠══╬══╬══╬══╬══╬══╬══╬══╬══╬══╣")
    print("║%s║%s║%s║%s║%s║%s║%s║%s║%s║%s║" % tuple(s[4]))
    print("╠══╬══╬══╬══╬══╬══╬══╬══╬══╬══╣")
    print("║%s║%s║%s║%s║%s║%s║%s║%s║%s║%s║ "% tuple(s[5]))
    print("╠══╬══╬══╬══╬══╬══╬══╬══╬══╬══╣")
    print("║%s║%s║%s║%s║%s║%s║%s║%s║%s║%s║" % tuple(s[6]))
    print("╠══╬══╬══╬══╬══╬══╬══╬══╬══╬══╣")
    print("║%s║%s║%s║%s║%s║%s║%s║%s║%s║%s║" % tuple(s[7]))
    print("╠══╬══╬══╬══╬══╬══╬══╬══╬══╬══╣")
    print("║%s║%s║%s║%s║%s║%s║%s║%s║%s║%s║" % tuple(s[8]))
    print("╠══╬══╬══╬══╬══╬══╬══╬══╬══╬══╣")
    print("║%s║%s║%s║%s║%s║%s║%s║%s║%s║%s║" % tuple(s[9]))
    print("╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝")

    # print(type(s[a-1][b-1]))
    # print(s[b-1][a-1:a+2])
    # print(s[a-1][b-1])


#
    # TODO 横排判断：Done

    for i in range(0, 6):
        for j in range(0, 6):
            if s[i][j:j+5] == ['X ', 'X ', 'X ', 'X ', 'X ']:
                print("X wins!")
            elif s[i][j:j+5] == ['O ', 'O ', 'O ', 'O ', 'O ']:
                print("O wins!")

    # TODO 竖排判断：Done

    for j in range(0, 6):
        for i in range(0, 6):
            if s[i][j] == s[i+1][j] == s[i+2][j] == s[i+3][j] == s[i+4][j] == 'X ':
                print("X wins!")
            elif s[i][j] == s[i+1][j] == s[i+2][j] == s[i+3][j] == s[i+4][j] == 'O ':
                print("O wins!")

    # TODO 斜排判断：Done

    for i in range(0, 6):
        for j in range(0, 6):
            if s[i][j] == s[i+1][j+1] == s[i+2][j+2] == s[i+3][j+3] == s[i+4][j+4] == 'X ':
                print("X wins!")
            elif s[i][j] == s[i+1][j+1] == s[i+2][j+2] == s[i+3][j+3] == s[i+4][j+4] == 'O ':
                print("O wins!")

    for j in range(4, 10):
        for i in range(0, 6):
            if s[i][j] == s[i+1][j-1] == s[i+2][j-2] == s[i+3][j-3] == s[i+4][j-4] == 'X ':
                print("X wins!")
            elif s[i][j] == s[i+1][j-1] == s[i+2][j-2] == s[i+3][j-3] == s[i+4][j-4] == 'O ':
                print("O wins!")


# use chess(a, b)
while True:
    a = input("row：")
    b = input("rank：")

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Please enter: ")
        continue
    if a not in range(1, 11) or b not in range(1, 11):
        print("Illegal! ")
        continue
    chess(a, b)
