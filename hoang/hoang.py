# a number number = 1234.9894894
# perform your magic here
#print(number)
# >>> Number got formatted to 1234.989#
'''number = input('tyoe your number here')
index = number.index('.')
print(number[:(index+3)])'''

# names = ['tega', 'my linh', 'charlie', 'shifu']
# ages = [23, 40, 27, 14]
# for i in range(0,len(names)):
#     print(f'{names[i]} is {ages[i]} years old')

# from random import randint


# answer = randint(1, 5)
# print("Guess must be within 1 and 5")

# try:
#     user_guess = int(input("Enter your guess: "))
# except ValueError:
#     print("Kindly enter a valid integer and try again")
# else:
#     if answer != user_guess:
#         print("You guessed wrong, the correct answer was", answer)
#     else:
#         print("Woah, that was an absolute stunner, correct!")
# finally:
#     print("I always get executed no matter what!")

# 1234.9894894 => 1234.989
# number = 1234.9894894
# perform your magic here
# print(number)
# >>> Number got formatted to 1234.989
# print("{0:.3f}".format(number))

# names = ['tega', 'my linh', 'charlie', 'sifu']
# ages = [23, 40, 27, 14]

# for name, age in zip(names, ages):
# print('%s is %d years old\n' % (name.upper(), age))
# print(F'{ name.upper() } is { age } years old\n')
# print('{} is {} years old\n'.format(name.upper(), age))
# print('{1} is {0} years old\n'.format(age, name.upper()))

# import time
# from datetime import datetime


# while True:
#     time.sleep(1)
#     current_time = datetime.now()
#     message = datetime.strftime(current_time, 'This is %H:%M:%S AM on %dth of %b and the year is %Y')
#     print(message)