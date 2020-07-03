class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getdata(self):
        return self.data

    def getnext(self):
        return self.next

    def setdata(self, newdata):
        self.data = newdata

    def setnext(self, newnext):
        self.next = newnext


class unorderlist:
    def __init__(self):
        # Node.__init__(self, initdata=self.data)
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setnext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getnext()

        return count

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current == item:
                found = True

            else:
                current = current.getnext()

        return found

    def remove(self, item):
        current = self.head
        found = False
        previous = None

        while current != 0 and not found:
            previous = current
            current = current.getnext()

            if current.getdata == item:
                found = True

            else:
                previous = current
                current = current.getnext()

        if previous == None:
            self.head = current.getnext()

        else:
            previous.setnext(current.getdnext())

