def fibonacci(n):
    if n in (0,1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(41):
    print(f'Fibonacci({n}) = {fibonacci(n):,d}')