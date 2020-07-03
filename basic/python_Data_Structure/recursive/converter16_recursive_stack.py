from pythonds.basic.stack import Stack


def tostr_2(num, base):
    rstack = Stack()
    digits = '0123456789ABCDEF'

    while num > 0:
        if num <= base:
            rstack.push(digits[num])

        else:
            rstack.push(digits[num % base])

        num = num // base

    temp = ''

    while not rstack.isEmpty():
        temp = temp + str(rstack.pop())

    return temp


print(tostr_2(1203, 16))
