import time
def sum(n):
    start = time.time()
    Firstnum = 0
    for n in range(n, n+1):
        Firstnum = Firstnum + 1
        end = time.time()


        return Firstnum, end-start

print(sum(8))