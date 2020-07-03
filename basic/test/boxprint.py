def boxprint(symbol, width, height):
    if len(symbol) != 1:
        print('Symbol must be a a single string')
    if len(width) <= 2:
        print('Width must be greater than 2')
    if len(height) <= 2:
        print('height must be greater than 2')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxprint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))



