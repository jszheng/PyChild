import timeit


def recMC(coinvaluelist, change):
    minCoin = change

    if change in coinvaluelist:
        return 1

    else:
        for i in [c for c in coinvaluelist if c <= change]:
            numCoin = 1 + recMC(coinvaluelist, change - i)
            if numCoin < minCoin:
                minCoin = numCoin

    return minCoin


# print(recMC([1, 5, 10, 25], 63))


def recDC(CoinValueList, change, KnownList):
    minCoin = change

    if minCoin in CoinValueList:
        KnownList[change] = 1
        return 1

    elif KnownList[change]>0:
        return KnownList[change]

    else:
        for i in [c for c in CoinValueList if c <= change]:
            numcoin = 1 + recDC(CoinValueList, change-i, KnownList)
            if numcoin < minCoin:
                minCoin = numcoin
                KnownList[change] = minCoin

    return minCoin


# print(recDC([1, 5, 10, 25], 63, [0]*64))


def dpMakeChange(CoinValuelist, change, mincoinlist):

    for cents in range(1, change + 1):
        mincoin = cents

        for i in [c for c in CoinValuelist if c <= cents]:
            if mincoinlist[cents - i] + 1 < mincoin:
                mincoin = mincoinlist[cents - i] + 1

        mincoinlist[cents] = mincoin

    return mincoinlist[change]


print(dpMakeChange([1, 5, 10, 21, 25], 63, [0]*64))




