#  list of Error 
#  1. compile Error --> Syntax errors detected before code execution 
#                           (missing colons, brackets, etc.)

#  2. logical Error --> Code runs without crashing but produces incorrect results due to flawed logic

#  3. Run time Error --> Code executes initially but crashes during execution 
#                       (e.g., division by zero, accessing undefined variables)




a = 5 
b =0
print (a/b)      # as we know we cant divide by zero it will show the error 

""" Error-> 
ZeroDivisionError: Division by zero
"""

print("bye")
#  Our code stops in between and never reaches to this statment to bypass this error 

"""we can use 'try' block"""
#  'try' block is use for trying to execute the critical statement ( the line of code not sure wether work or not)


"""FINAL version """

while True:
	try:
		a = int(input("Enter 1st: "))
		b = int(input("Enter 2nd: "))
		print("\n........")
		print(a/b)      # like i said it will try to execute but in case there is an actual error then 
	except ZeroDivisionError as e:             # we use except for exception ,  the moment no error found it will run peacefully
			print("hey, can't divide by zero dumbass..." ,e)

	except Exception as e:
			# exception block - for handling any error 
			print(" Error causing : ",e)

	finally:             #this block is use for executing whether u get error or not 
			print(".........")

	print("\nbye, fucker!!\n")  


"""
why we using the 'finally block' because try jumps out of it whenever sees the error 
and we can loose the bunch of codes  that's why , we use 'finally' 
to avoid this situation because the after the crictical statment , work or not 'finally' will work
"""