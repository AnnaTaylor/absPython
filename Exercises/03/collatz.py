# Write a function named collatz() that has one parameter named number. If 
# number is even, then collatz() should print number // 2 and return this value.  
# If number is odd, then collatz() should print and return 3 * number + 1.
#
# Then write a program that lets the user type in an integer and that keeps 
# calling collatz() on the number until the function returns the value 1. This 
# sequence works for any integer - sooner or later, using this sequence, you'll 
# arrive at 1! Even mathematicians aren't sure why...
#
# Part II - Input Validation
# Add try and except statements to the program to detect whether the user types 
# in a noninteger string. Normally the int() function will raise a ValueError if 
# it is passed a noninteger string. In the except clause, print a message to the 
# user saying they must enter an integer.
import sys

def collatz(number):
	if number % 2 == 0:
		output = number // 2
		print(output)
		return output
	else:
		output = (3 * number) + 1
		print(output)
		return output

def prettyPrint(list):
	listLength = len(list)
	for i in range(listLength):
		print(list[i])



# Main program
messages = ["Welcome to Collatz", "Enter a number"]
prettyPrint(messages)
errorState = True
while errorState:
	try:
		result = collatz(int(input()))
		errorState = False
	except ValueError:
		print("Please enter an integer value")
		continue
	
while result != 1:
	result = collatz(result)



sys.exit()
