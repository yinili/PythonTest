def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
    return 'well done'

f = fib(5)
print(list(f))