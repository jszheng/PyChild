from pythonds.basic.stack import Stack


def parChecker(symbolString):
    s = Stack()
    balance = True
    index = 0

    while index < len(symbolString) and balance:
        symbol = symbolString[index]

        if symbol in '([{':
            s.push('(')

        else:
            if s.isEmpty():
                balance = False

            else:
                top = s.pop()
                # if not matches(top, symbol):
                if top != symbol:
                    balanced = False

        index = index + 1

    if balance is True and s.isEmpty():
        return True

    else:
        return False

# def	matches(open,close):
#     opens = "([{"
#     closers = ")]}"
#     return opens.index(open) == closers.index(close)


print(parChecker('((()))'))
print(parChecker('((())'))

print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))
print(parChecker('[[{()}]]'))





