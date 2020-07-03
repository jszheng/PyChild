class Queue:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def enqueue(self, items):
        return self.item.insert(0, items)

    def size(self):
        return len(self.item)

    def dequeue(self):
        return self.item.pop()

