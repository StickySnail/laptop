def power(x, y):
    # 코드를 작성하세요.

    if x == 1:
        return 1
    elif y == 1:
        return x
    else:
        return x*power(x,y-1)

# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))