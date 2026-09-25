cars = 100 # assigning 100 to the variable cars
space_in_a_car = 4.0 # assigning 4.0 to the variable space_in_a_car
drivers = 30 # assigning 30 to the variable cars
passengers = 90 # assigns 90
cars_not_driven = cars - drivers # assigns to cars_not_driven the result of the value of cars minus drivers (100-30)
cars_driven = drivers # assings the value of drivers to cars_driven
carpool_capacity = cars_driven * space_in_a_car # carpool_capacity has value 30*4.0
average_passenger_per_car = passengers / cars_driven # average_passenger_per_car has value 90 / 30

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passenger_per_car,
      "in each car.")

"""
STUDY DRILLS
1. I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
2. Remember that 4.0 is a floating point number. 
It's just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating point.
3. Write comments above each of the variable assignments.
4. Make sure you know what = is called (equals) and that its purpose is to give data (numbers, strings, etc.) names (cars_driven, passengers).
5. Remember that _ is an underscore character.

SOLUTIONS
1. No, the use of 4.0 is not necessary, if instead of that you use 4 the result will be an integer and not a float.
so the result of carpool_capacity will be 120 instead of 120.0 . 
"""