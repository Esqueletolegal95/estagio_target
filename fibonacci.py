def fibonacci(num):
    fib1 = 0
    fib2 = 1
    while num < fib1 + fib2:
        fib1, fib2 = fib2, fib1+fib2
    if num = fib1+fib2 :
        return True
    else:
        return False
