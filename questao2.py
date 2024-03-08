def fibonacci(num):
    fib1 = 0
    fib2 = 1
    while num > fib1 + fib2:
        fib1, fib2 = fib2, fib1+fib2
    if num == fib1+fib2:
        return True
    else:
        return False


numero = int(input("digite um numero"))
if fibonacci(numero):
    print(str(numero) + " pertence a sequencia")
else:
    print(str(numero) + " nao pertence a sequencia")