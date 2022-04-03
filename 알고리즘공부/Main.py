def sorting(list):
    for n in range(len(tmp_list)):
        for i in range(n):
            if tmp_list[i] <= tmp_list[i+1]:
                continue
            else:
                tmp = tmp_list[i]
                tmp_list[i] = tmp_list[i+1]
                tmp_list[i+1] = tmp
    return tmp_list


tmp_list = [5,3,2,7,8,3,5,5,3,9]
print(sorting(tmp_list))
