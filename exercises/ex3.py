print("I will now count my chickens:") # This line print a string

print("Hens",25 + 30 / 6) # This line prints a str, and the solution of the math: 30/6 + 25
print("Roosters",100 - 25 * 3 % 4) # Prints a str, and the solution of the math: 100-(25*3 % 4) = 100 - 3 = 97 (75 % 4 gives the rest of the division)

print("Now I will count the eggs:") # prints a str

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6 ) # prints the solution of the math: 6 - 5 + 0 - 0.25 + 6 = 6.75

print("Is that true that 3 + 2 < 5 - 7?") # prints a str

print(3 + 2 < 5 - 7) # prints True or False based on the comparision of the solution of the two operations, 5 is greater than -2 so is False 

print("What is 3 + 2?",3 + 2) # prints the str, and the math
print("What is 5- 7?",5 - 7) # prints the str, and the math

print("Oh, that's why is False.") # prints a str

print("How about some more.") # prints a str

print("Is it greater?",5 > -2) # prints a str and True because 5 is greater than -2
print("Is it greater or equal?",5 >= -2) # prints a str and True because 5 is grater or equal compared to -2
print("Is it less or equal?", 5 <= -2) # prints a str and False because 5 is not less or equal than -2

"""
STUDY DRILLS
1. Above each line, use the # to write a comment to yourself explaining what the line does.
2. You can type most math directly into a Jupyter cell and get results. Try using it to do some basic calculations like 1+2 and hit SHIFT-ENTER.
3. Find something you need to calculate and write a new .py file that does it.
4. Rewrite this exercise to use floating point numbers so it's more accurate. 20.0 is floating point.

SOLUTIONS
"""

print("I will count my chickens:")

print("Hens", 25.00 + 30.00 / 6.00)
print("Roosters", 100.00 - 25.00 * 3.00 % 4.00)

print("Now I will count the eggs:")
print(3.00 + 2.00 + 1.00 - 5.00 + 4.00 % 2.00 - 1.00 / 4.00 + 6.00 )

print("Is it true that 3 + 2 < 5 - 7?")

print(3.00 + 2.00 < 5.00 - 7.00)

print("What is 3 + 2?", 3.00 + 2.00)
print("What is 5 - 7?", 5.00 - 7.00)

print("Oh, that's why it's False.")
print("How about some more.")

print("Is it greater?", 5.00 > -2.00)
print("Is it greater or equal?", 5.00 >= -2.00)
print("Is it less or equal?", 5.00 <= -2.00)