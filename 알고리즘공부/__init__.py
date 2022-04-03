
def linear_search(element, some_list):
    for i in range(len(some_list)):
        if element == some_list[i]:
            return i
        None

def binary_search(element, some_list):
    first_index = 0
    last_index = len(some_list)-1 #4
    mid_index = (first_index + last_index)//2




print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))