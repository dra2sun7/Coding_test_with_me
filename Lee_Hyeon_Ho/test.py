def fib_op(n):
    a, b = 1, 0
    for _ in range(n-1):
        print(f"a, b : {a} {b}")
        tmp = a
        a = a + b
        b = tmp
    return a

print(fib_op(10))