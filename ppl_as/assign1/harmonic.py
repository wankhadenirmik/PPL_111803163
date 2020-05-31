# Python3 program to check if the 
# given number is Ore number 
arr =[]
n = int(input("enter the starting no from which u want to count harmonic divisor: "))
j = 0
while j != 10: 
	for i in range(1, int(n**(0.5)) + 1): 
		if n % i == 0: 		
			if n // i == i: 
				arr.append(i) 
			else: 
				arr.append(i) 

				arr.append(n // i) 
		
	Sum = 0
	length = len(arr) 
	for i in range(0, length): 
		Sum = Sum + (n / arr[i]) 

	Sum = Sum / n

	mean =  length / Sum
	if mean - int(mean) == 0: 
		print(n)
		j =j + 1
	else: 
		pass
	n = n + 1
	arr.clear()


