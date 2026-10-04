types_of_people = 10 # assign 10 to a variable 
x = f"There are {types_of_people} types of people." # variable that contains an f-string, in the string there is a variable 

binary = "binary" # variable that has a string
do_not = "don't" # variable that has a string
y = f"Those who know {binary} and those who {do_not}." # variable that contains an f-string, in the string there are two variables # here there are two strings inside a string

print(x) # print x that is a variable with an f-string
print(y) # print y that is a variable with an f-string

print(f"I said: {x}") # print an f-strng that contains a variable with an f-string # here there is a string inside a string
print(f"I also said: '{y}'") # print an f-string that contains a variable with an f-string # here there is a string inside a string

hilarious = False # the variable is set to false
joke_evaluations = "Isn't that joke so funny?!{}" # this variable has a string with a {} at the end

print(joke_evaluations.format(hilarious)) # print a variable that contains a string and call on thet the metod .format that insert in strings placeholders what is specificated in the parameter
# up here there is a string inside a string

w = "This is the left side of..." # variable with string
e = "a string with a right side." # variable with string

print(w + e) # print the addition of two strings

"""
STUDY DRILLS
1. Go through this program and write a comment above each line explaining it.
2. Find all the places where a string is put inside a string.
3. Are you sure there are only four places? How do you know? Maybe I like lying.
4. Explain why adding the two strings w and e with + makes a longer string. 

SOLUTIONS
3. There are five places because Hilarius became a string when method format() is called.
4. Becouse python joins the strings with the symbol +"""