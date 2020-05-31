import random
print("number from the dice")
print(random.randrange(1,7))
choice = input("Do you want quit ? yes / no :")

while(choice != "yes") :
	print("\nnumber from the dice")
	print(random.randrange(1,7))
	choice = input("Do you want quit ? yes / no :")
	
print("exit!! Thank you!!")