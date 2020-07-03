class BinaryTree:
    def __init__(self, rootobj):
        self.key = rootobj
        self.leftchild = None
        self.rightchild = None

    def insertleft(self, newNode):
        if self.leftchild == None:
            self.leftchild = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.leftchild = self.leftchild
            self.leftchild = t

    def insertright(self, newNode):
        if self.rightchild ==  None:
            self.rightchild = newNode

        else:
            t = BinaryTree(newNode)
            t.rightchild = self.rightchild
            self.rightchild = t

    def getleftchild(self):
        return self.leftchild

    def getrightchild(self):
        return self.rightchild

    def setrootval(self, obj):
        self.key = obj

    def getrootval(self):
        return self.key

