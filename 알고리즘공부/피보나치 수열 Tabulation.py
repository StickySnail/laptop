def fib_tab(n):
    fib = []
    fib.append(1)
    fib.append(1)
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])

    return fib[n-1]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))