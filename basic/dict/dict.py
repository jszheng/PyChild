birthdays = {'Alice': 'April 1', 'Bob': 'Jan 1'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == "":
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of' + name)
    else:
        print('I don not have the birthday information of' + name)
        print('what is the birthday of him/her')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')


spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)



import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)


"""

"""

# tictactoe
theBoard = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
            'low-l': ' ', 'low-m': ' ', 'low-r': ' '}


def printBoard(board):
    print(theBoard['top-l'] + '    |    ' + theBoard['top-m'] + '    |    ' + theBoard['top-r'])
    print('-----+---------+-----')
    print(theBoard['mid-l'] + '    |    ' + theBoard['mid-m'] + '    |    ' + theBoard['mid-r'])
    print('-----+---------+-----')
    print(theBoard['low-l'] + '    |    ' + theBoard['low-m'] + '    |    ' + theBoard['low-r'])


turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    if move not in theBoard:
        print('ERROR')
        continue
    if (theBoard[move] == 'X') or (theBoard[move] == 'O'):
        print('ERROR')

        continue

    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)

'''
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought += v.get(item, 0)
    return numBrought


print('Number of things being brought:')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))


while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        print('Thank you')
        break
print('Passwords can only have letters and numbers.')


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)


import pyperclip
pyperclip.copy('hello world')
pyperclip.paste()

'''

























