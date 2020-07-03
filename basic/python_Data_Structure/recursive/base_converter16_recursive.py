def tostr(num, base):
    digits = '0123456789ABCDEF'

    if num < base:
        return digits[num]

    else:
        return tostr(num//base, base) + digits[num % base]

print(tostr(79, 2))
print(tostr(30, 16))
