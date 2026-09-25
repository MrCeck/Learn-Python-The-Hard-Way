my_name = "Zed A. Shaw"
my_age = 35 # Not a lie
my_height = 74 # Inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky; try to get it exactly right
total = my_age + my_height + my_weight
print(f"if i add {my_age}, {my_height}, and {my_weight} I get {total}.")

"""
STUDY DRILLS
1. Change all the variables so there is no my_ in front of each one. Make sure you change the name everywhere, 
not just where you used = to set them.
2. Try to write some variables that convert the inches and pounds to centimeters and kilograms. 
Do not just type in the measurements. Work out the math in Python.
"""

# solutions
name = "Marco Cecchetto"
age = 23
height = 180 # cm
weight = 85 # kg
eyes = "green"
teeth = "white"
hair = "brown"

inches_to_cm = my_height * 2.54
cm_to_inches = height / 2.54
pound_to_kg = my_weight / 2.205
kg_to_pound = weight * 2.205

print(f"Let's talk about {name}.")
print(f"He's {height} cms tall.")
print(f"He's {weight} kg heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"if i add {age}, {height}, and {weight} I get {total}.")

print(inches_to_cm, cm_to_inches, pound_to_kg, kg_to_pound)