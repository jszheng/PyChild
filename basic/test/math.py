class method:
    set_A = [2, 4, 6, 8, 10]
    set_B = [1, 2, 4, 8, 16]
    set_P = []
    set_Q = []
    tup = ()
    union = []

    def __init__(self, A, B, P, Q, t, u):

        self.set_A = A
        self.set_B = B
        self.set_P = P
        self.set_Q = Q
        self.union = u
        self.tup = t

    for ele_B in set_B:
        union.append(ele_B)
    for ele_A in set_A:
        if ele_A not in set_B:
            union.append(ele_A)



