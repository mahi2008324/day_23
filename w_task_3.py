n=int(input("Enter the number : "))
def factorial():
	mul=1
	for i in range(1,n+1):
		mul=mul*i
	print("{} factorial(!) is {} " .format(n,mul))
factorial()