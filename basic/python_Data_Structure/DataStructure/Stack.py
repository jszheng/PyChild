class Stack:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def push(self, i):
        return self.item.append(i)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[len(self.item) - 1]

    def size(self):
        return len(self.item)


