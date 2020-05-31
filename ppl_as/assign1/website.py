#Build an application that can be used to block certain websites from opening.
file_path = "C:\Windows\System32\drivers\etc\hosts"
redirect_ip = "127.0.0.1"
website = str(input("Enter the website you want to block.\n"))
#context manager
with open(file_path, 'r+') as file :
	cont = file.read()
	if website in cont :
		print("Website is already blocked.\n")
		pass
	else :
		file.write(redirect_ip + " " + website + "\n")
		print("Website blocked.\n")