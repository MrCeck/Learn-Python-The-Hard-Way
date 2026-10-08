tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t*Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

"""
STUDY DRILLS
1. Memorize all the escape sequences by putting them on flash cards. 
2. Use ''' (triple-single-quote) instead. Can you see why you might use that instead of \"""?
3. Combine escape sequences and format strings to create a more complex format."""

slim_dog = '''
I see, I can use triple-single quotes and add inside 
\t"""a triple-double quote"""
\'and now I play with some escape\'
\t\vok\n\t\b\\one\\\n\t\""two"\"\n\t\b\b\'\''three''\'
\anot sure\n\feven more
            \rnow I'm sure
        \r\t\tof course
'''
print(slim_dog)
drill2 = "Ok now I\'m trying with {},\nIt seems to \twork\n\t\vI believe"
print(drill2.format("an f-string"))
print(f"But I can go even like this\nand do some mix\tup\n\v{persian_cat}")