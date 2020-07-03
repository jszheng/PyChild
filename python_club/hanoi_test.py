def hanoi(n, x, y, z):
    if n == 1:
        # print(x, '-->', z)
        print(x, '-->', z)

    else:

        hanoi(n - 1, x, z, y)
        print(x, "-->", z)
        hanoi(n - 1, y, x, z)


while True:
    n = input('levels：')
    if n == '':
        break
    else:
        print(hanoi(int(n), 'x', 'y', 'z'))


