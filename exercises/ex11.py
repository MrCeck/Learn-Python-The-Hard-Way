print("How old are you?", end='')
age = input()
print("How tall are you?", end='')
height = input()
print("How much do you weigh?", end='')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

"""
STUDY DRILLS
1. Go online and find out what Python's input does. 
2. Can you find other ways to use it? Try some of the samples you find. 
3. Write another “form” like this to ask some other questions.

SOLUTION
1. input() is a built-in function that reads an input from the user and converts it to a string and returns that. 
"""
from random import randint
x = randint(1, 5)
while True:
    y = int(input("guess the number >>>"))
    if x == y:
        break

print("What's your pet name?", end='')
cat = str(input(">>> "))
bday = str(input("When is your bday? "))
food = input("what's your favorite food? ")

print(f"Your pet name is {cat}, your birthday is {bday} and your favorite food is {food}.")