from random import randint

# Variables
count = 4;
random = randint(1,20)

# while loop
while count != 0 :
    answer = int(input(f"You have {count} chances."
                     f" choose a number between 1 and 20: "))

    if answer == random :
        print(f"Congratuations! you made it within {3-count} times")
        break
    elif answer > random :
        print("Down")
        count -= 1
        continue
    elif answer < random :
        print("Up")
        count -= 1
        continue

if count == 0:
    print(f"Sorry. the answer was {random}.")










