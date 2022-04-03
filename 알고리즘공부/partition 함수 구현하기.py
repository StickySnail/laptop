# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    tmp = my_list[index2]
    my_list[index2] = my_list[index1]
    my_list[index1] = tmp


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 코드를 작성하세요.
    big = start
    unknown = start
    pivot = end

    while unknown < pivot:
        if my_list[pivot] < my_list[unknown]:
            unknown += 1
        elif my_list[pivot] >= my_list[unknown]:
            swap_elements(my_list,big, unknown)
            big += 1
            unknown += 1

    if len(my_list[unknown:pivot]) < 1:
        swap_elements(my_list, big, pivot)
        tmp = pivot
        pivot = big
        big = tmp
        return pivot



# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)
