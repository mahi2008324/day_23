a=list(input("Enter the list elements : "))
def remove_duplicate(a):
	b=set(a)
	c=list(b)
	c.sort()
	return(c)
print(remove_duplicate(a))