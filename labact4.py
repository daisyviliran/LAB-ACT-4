def classify_age(age):
	if age < 0:
		print("invalid age. please enter a positive number.")
	elif age <= 12:
		print("you are a child.")
	elif age <= 19:
		print("you are a teen.")
	elif age <= 64:
		print("you are an adult.")
	else:
		print("you are a senior.")
		
while True:
	age = int(input("enter your age: "))
	classify_age(age)