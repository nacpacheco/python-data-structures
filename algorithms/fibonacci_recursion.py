# Exponential time complexity O(2^N) 
# recursive algorithms tava solve a problem of n
# Not ideal solution (can be better with dynamic programmin To be continued...)
def fibonacci_recursion(n):
    if n < 2:
        return n
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

# O(N)
def fibonacci_iterative(n):
    fib = [0,1]
    for i in range(2,n+1):
        fib.append(fib[i-2]+fib[i-1])
    return fib[n]

print(fibonacci_recursion(8))
print(fibonacci_iterative(8))