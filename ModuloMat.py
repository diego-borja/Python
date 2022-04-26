def esPrimo(n):
    for x in range(2, (n//2)+1):
        if n%x == 0:
            return False
    return True

def factorial(n):
    f = 1
    for i in range(2,n+1):
        f *= i
    return f