def binarytree(r):
    return [r, [], []]


def insertleft(root, newbranch):
    n = root.pop(1)

    if len(n) > 1:
        root.insert(1, [newbranch, n, []])

    else:
        root.insert(1, [newbranch, [], []])

    return root


def insertright(root, newbranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newbranch, [], t])

    else:
        root.insert(2, [newbranch, [], []])

    return root


def getrootvalue(root):
    return root[0]


def setrootvalue(root, newvalue):
    root[0] = newvalue


def getleftchild(root):
    return root[1]


def getrightchild(root):
    return root[2]



