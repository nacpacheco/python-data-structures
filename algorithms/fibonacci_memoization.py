
def fibonacci_recursion(n):
    if n < 2:
        return n
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def fibonacci_master():
    cache = {}
    def fib(n):
        if n in cache.keys():
            return cache[n]
        else:
            if n < 2:
                return n
            else:
                cache[n] = fib(n-1) + fib(n-2)
                return cache[n]
    return fib

faster_fib = fibonacci_master()
print(faster_fib(10))
