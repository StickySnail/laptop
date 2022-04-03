def sublist_max(profits):
    # 코드를 작성하세요.
    output = 0
    for left in range(len(profits)-1):
        for right in range(left, len(profits)):
            output = max(output, sum(profits[left:right+1]))
    return output



# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))