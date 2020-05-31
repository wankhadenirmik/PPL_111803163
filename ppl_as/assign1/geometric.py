#geometric series 10 numbers
a = input("Enter first term-")
b = input("Enter common ratio-")
a = int(a)
b = int(b)
i = 0
while i < 10 :
	print(a*pow(b,i))
	i = i +1