class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, item):
        return self.items.insert(0, item)

    def addFront(self, item):
        return self.items.append(item)

    def size(self):
        return len(self.items)

    def removeRear(self, item):
        return self.items.pop(item, 0)

    def removeFront(self, item):
        return self.items.pop(item)

    