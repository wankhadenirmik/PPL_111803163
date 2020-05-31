# armstrong numbers
a = input("starting no: ")
b = input("ending no: ")
A = int(a) 
B = int(b)
def armstrong(n):
	m = n
	sum = 0
	while m != 0 :
		sum = sum + ((m % 10)**3)
		m = int(m / 10)
	if sum == n :
		return 1
	else :
		return 0
		

while A != B + 1 :
	if armstrong(A) == 1 :
		print(A)
	A = A + 1