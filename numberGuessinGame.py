import random

print('___Welcome to number guessing game___')
name = input('Enter your name before we play ')

count = 1
random_num = int(random.randint(1, 10))
while True:
    user_num = (input(f'Enter your guess from 1 to 10 '))
    if user_num.isdigit():
        user_num = int(user_num)
    else:
        print("Please type a number between 0 to 10")
        continue

    if user_num == random_num:
        break
    elif user_num > random_num:
        user_num = (print("Oops! Guess lower "))
    else:
        user_num = (print("Oops! Guess Higher "))
    count += 1
print(f'Congrats,{name} you have successfully guessed the number in {count} try:)')
