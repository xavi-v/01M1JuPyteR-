def fib(n):
    """
    Serie de Fibonacci hasta n
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

def fib2(n):   
    """
    Serie de Fibonacci hasta n
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result