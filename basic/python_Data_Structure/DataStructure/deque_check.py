from pythonds.basic.deque import Deque

def palchecker(symbolstring):
    chardeque = Deque()
    stillequal = True

    for string in symbolstring:
        chardeque.addRear(string)

    while chardeque.size() > 1 and stillequal:
        front = chardeque.removeFront()
        end = chardeque.removeRear()

        if end != front:
            stillequal = False

        return stillequal


print(palchecker("lsdkjfskf"))
print(palchecker("radar"))






