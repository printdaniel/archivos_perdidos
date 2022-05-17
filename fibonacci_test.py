import time
n = int(input("Ingrese n: "))

def fib_recursivo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursivo(n-1) + fib_recursivo(n-2)

def fib_dinamico (n, cache = {0:0,1:1}):
    if n in cache:
        return cache[n]
    cache[n] = fib_dinamico(n-1) + fib_dinamico(n-2)
    return cache[n]

start = time.time()
print(fib_recursivo(n))
end = time.time()
print((end - start)*1000)


start = time.time()
print(fib_dinamico(n))
end = time.time()
print((end-start)*1000)

