a=int(input("Enter value 1 : "))
b=int(input("Enter value 2 : "))
c=int(input("Enter value 3 : "))
def max_value(a,b,c):
	if a>b and a>c:
		print(a," is greater")
	elif b>a and b>c:
		print(b," is greater")
	else:
		print(c," is greater")
max_value(a,b,c)