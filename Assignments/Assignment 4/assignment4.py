#Write a function which will sum a range of integers starting from one going up and
including a value entered by the user. Return the sum.

start = int(input("Starting Number: "))
length = int(input("Amount of Numbers added: "))
sum = 0

def addition(x, y):
	return x + y 

while sum < length:
	yes = start + 1
	yes += 1
	sum += 1
print(addition(start, yes))



#Write a main function which takes a number entered by the user and calls the function,
outputting the result to the user with a print statement.

print("\n")
fav_num = int(input("Favorite Number: "))

def number():
	if fav_num < 11:
		print("Your Future: You will fail a test soon.")
	elif fav_num < 21:
		print("Your Future: You will find money on the ground.")
	elif fav_num < 41:
		print("Your Future: You will get in a car crash.")
	elif fav_num < 61:
		print("Your Future: You will die your hair soon.")
	else:
		print("Your Future: You will meet someone famous soon.")

number()



