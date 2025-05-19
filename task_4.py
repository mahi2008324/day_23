a=str(input("Enter the string : "))
b="AEIOUaeiou"
c=[]
for x in a:
	if x in b:
		c.append(x)
print(c)