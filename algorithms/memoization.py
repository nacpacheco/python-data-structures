def simpleaddTo80(n):
    return n + 80


def memoizedAddTo80():
    cache = {}
    def addTo80(n):
        if n in cache.keys():
            return print('cache ' + str(cache[n]))
        else:

            cache[n] = n + 80
            return print('long time ' + str(cache[n]))
    return addTo80

memo5 = memoizedAddTo80()
memo5(5)
memo5(5)