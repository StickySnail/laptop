def Hansu(a):
    count = 99
    for i in range(100, a + 1):
        a = i // 100
        b = i % 100 // 10
        c = i % 10
        if 2 * b == a + c:
            count += 1
    if a == 1000:
        count -= 1
    return count


num = input()
num = int(num)
if num > 99:
    print(Hansu(num))
else:
    print(num)
