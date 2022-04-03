# 파라미터 some_list를 거꾸로 뒤집는 함수
new_list=[]
def flip(some_list):
    if len(some_list) == 1 or len(some_list)== 0:
        return some_list
    return some_list[-1:] + flip(some_list[:-1])

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

some_list = flip(some_list)
print(some_list)
# '-'의 슬라이싱 범위 숙지
print(some_list[:-1])