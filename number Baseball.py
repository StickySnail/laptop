from random import randint
number_computer = []
number_user = []
count = 1

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
i = 0
while i < 3:
    num = randint(0,9)
    if num in number_computer:
        continue
    else:
        number_computer.append(num)
        i += 1


while True:
    i = 0
    print("세 수를 하나씩 차례대로 입력하세요.")
    while i < 3:
        num = int(input(f"{i+1}번째 수를 입력하세요: "))
        if num > 9 or num < 0 :
                print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
                continue
        elif num in number_user:
            print("중복되는 수 입니다. 다시 입력해주세요.")
            continue
        else :
            number_user.append(num)
            i += 1


    i = 0
    s = 0
    b = 0


    while i < 3 :
        if number_computer[i] == number_user[i]:
            s += 1
        elif number_computer[i] in number_user:
            b += 1
        i += 1


    print(f"{s}S {b}B")
    print("")
    if s == 3 :
        print(f"축하합니다. {count}번만에 세 숫자의 값과 위치를 모두 맞추셨습니다.")
        break
    else :
        number_user = []
        count += 1
        continue




