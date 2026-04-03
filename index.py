# BU Demo - Written by Browser Use Agent
import datetime

def greet(name):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'Hello {name}! BU says hi at {now}'

def fibonacci(n):
    if n <= 0:
        return []
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

if __name__ == '__main__':
    print(greet('kozzy'))
    print(f'Fibonacci(10): {fibonacci(10)}')
