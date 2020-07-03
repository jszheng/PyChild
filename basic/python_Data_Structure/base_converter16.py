from pythonds.basic.stack import Stack


def base_converter(symbolInteger, base):
    digits = '0123456789ABCDEF'
    rem_stack = Stack()

    while symbolInteger > 0:
        rem = symbolInteger % base
        rem_stack.push(rem)
        symbolInteger = symbolInteger//base


    newstring = ''
    while not rem_stack.isEmpty():
        newstring = newstring + digits[rem_stack.pop()]

    return newstring


if __name__ ==  '__main__':
    print(base_converter(453986, 16))
