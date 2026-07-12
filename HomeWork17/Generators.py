print ("first task")

def fibonacci_generator(n):
    a, b = 0, 1

def even_numbers_generator(n):
    for i in range(0, n + 1, 2):
        yield i


for num in even_numbers_generator(10):
    print(num)

print ("second task")

def fib(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


for num in fib(10):
    print(num)