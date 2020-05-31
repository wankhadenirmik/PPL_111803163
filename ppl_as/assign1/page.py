import array 
   

page = []
print("Enter total Number of pages")
N = int(input())
print("Enter page number list")

count = 1
while count <= N :
	k = int(input())
	
	if k != -1 :
		page.append(k)
	else :
		break
	count = count + 1
print("missing pages are-")
count = 1
while count <= N :
	if page.count(count) == 0 :
		print(count)
	count = count + 1
	
