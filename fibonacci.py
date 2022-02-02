# %%
# def fibonacci(n):
#     if n < 3:
#         return 1

#     return fibonacci(n - 1) + fibonacci(n - 2)

# fib_30 = fibonacci(30)
# f"the 30th Fibonacci number is {fib_30}"
# %%
cache = {}


def fibonacci(n):
    if n < 3:
        return 1

    if n in cache:
        return cache[n]

    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]


fib_50 = fibonacci(50)
f"the 50th fibonacci number is {fib_50}"