def fib_optimized(n):
    current = 1
    previous = 0

    for i in range(1,n):
        tmp = current
        current += previous
        previous =tmp
        # (Easy way) current, previous = current + previous, current

    return current

# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
