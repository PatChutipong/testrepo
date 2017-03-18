number = raw_input("Enter a fucking number:")

def factorial(number):
	if(number<=1):
		return 1
	else:
		return number*factorial(number-1)

print factorial(int(number))