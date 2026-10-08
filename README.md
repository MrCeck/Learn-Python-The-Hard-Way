# Learn-Python-The-Hard-Way
This is my repo for all the exercises in the book Learn Python The Hard Way by Zed Shaw.

## Overview
This repository contains my personal solutions and notes for the exercises from the book **"Learn Python The Hard Way"** (5th Edition) by Zed Shaw.

The goal of the repo is to document my progress as I learn Python and build a habit of daily version control with Git and GitHub.

## Enviroment & Tools
* **Language:** Python 3.13+
* **Editor:** Visual Studio Code
* **OS:** Windows

## Exercises 
Below you'll find notes on each exercise I completed, including the key concepts I learned and my answers to some of the Study Drills.

---

### Ex 01: Print

<details>
<summary> <b> Study Drills & Notes (Click to expand) </b> </summary>

#### What I Learned
In this exercise I got familiar with the use of print(), and learned how to use the comments(#) in python. 

</details>

### Ex 02: Comment

<details>
<summary> <b> Study Drills & Notes (Click to expand) </b> </summary>

#### What I Learned 
In this exercise I found out about the hash character and some type of review I can do on my code to check if there are sone errors.

</details>

### Ex 03: Math

<details>
<summary> <b> Study Drills & Notes (Click to expand) </b> </summary>

#### What I Learned 
In this exercises I understood how math and operator works in python, the order for resolution in expression and comparison with greater or less.

These are the symbols and what they do:
* **+ plus:** does the addition.
* **- minus:** does the subtraction.
* **/ slash:** does the division.
* **asterisk * :** does the multiplication.
* **% percent:** does the the divison between two numbers and gives back the remaining part of it. Ex. 10 divided by 3 is 3 with remaining of 1.
* **< less-than:** gives true if the first number is less than the second.
* **> greater-than:** gives true if the first number is greater than the second.
* **<= less-than-equal:** gives true if the first number is less or equal than the second.
* **>= greater-than-equal:** gives true if the first number is greater or equal than the second.
</details>

### Ex 04: Variables and Names

<details>
<summary> <b> Study Drills & Notes (Click to expand) </b> </summary>

#### What I Learned 
In this exercise I learned how to assign values to a variable, that can be an integer, a floating point, a string other variables or the result of some variables with math operators.
</details>

### Ex 05: More Variables and Printing

<details>
<summary> <b> Study Drills & Notes (Click to expand) </b> </summary>

#### What I Learned 
In this exercise I practiced more usage of Variables and I have done more printing 
</details>

### Ex 06: Strings and Text

<details>
<summary> <b> Study Drills & Notes (Click to expand) </b> </summary>

#### What I Learned 
In this exercise I learned how to use f-string, and how we can nest them,
I also learned the method *.format()*: 

This method can insert variables, strings or numbers in a palceholder inside the string of a variable. Placeholder are defined by: {}

I also learned how join two string: using the sybol + we can make one string out of two or more.
</details>

### Ex 07: Combining Strings 

<details>
<summary> <b> Study Drills & Notes (Click to expand) </b> </summary>

#### What I Learned 
In this exercise I learned how to add more variables that contain strings, and the use of end="": adds the value specificated and makes the next print on the same line, just after the value specificated  
</details>

### Ex 08:  Formatting String Manually 

<details>
<summary> <b> Study Drills & Notes (Click to expand) </b> </summary>

#### What I Learned 
In this exercise I learned how to use .format(), using a variable that has some placeholder inside.  
</details>

### Ex 09:  Multi-Line Strings

<details>
<summary> <b> Study Drills & Notes (Click to expand) </b> </summary>

#### What I Learned 
In this exercise I learned that we can print strings on multiple lines. 
We can use the new line character \n that makes the text continue after it on the next line.
We can also use the multiline string using """ """, the text inside will be printed exactly as it is written.
</details>

### Ex 10:  Escape Codes in Strings

<details>
<summary> <b> Study Drills & Notes (Click to expand) </b> </summary>

#### What I Learned 
In this exercise I learned how to use some escape sequences that allow us to insert certain characters inside strings without raising an error.

Here are some escape sequences:
* \\\ -> Backslash (\\)
* \\' -> Single-quote (')
* \\" -> Double-quote (")
* \a -> ASCII bell, can produce sounds
* \b -> ASCII backspace
* \f -> ASCII formfeed, used for printing text with printers
* \n -> linefeed
* \N{name} -> Character named name in the Unicode database
* \r -> Carriage return, move the cursor back to the start of the line
* \t -> Horizontal Tab
* \v -> Vertical Tab
* \uxxxx -> Character with 16-bit hex value
* \Uxxxxxxxx -> Character with 32-bit hex value
* \ooo -> Character with octal value
* \xhh -> Character with hex value  
</details>

### Ex 11:  Asking People Questions

<details>
<summary> <b> Study Drills & Notes (Click to expand) </b> </summary>

#### What I Learned 
In this exercise I learned how to use the built-in function input(), this function takes from the terminal a text-prompt from the user types, return its as a string. If we use int(input()) the function don't gives back a string but an integer thanks to the int() function. 
</details>

### Ex 12:  An Easier Way to Prompt

<details>
<summary> <b> Study Drills & Notes (Click to expand) </b> </summary>

#### What I Learned 
In this exercise I learned that I can use the input() function directly with a string inside to print something in the terminal correlated to the input prompt. 

I also learned that I can check documentation of function directly from the by hovering the cursor over it, or using the python terminal and using help().
I tried with help(print) and I found out that it takes objects and prints it on the text stram file. All the non-keyword arguments are converted to strings. 
</details>