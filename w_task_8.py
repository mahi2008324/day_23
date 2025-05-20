a=int(input("Enter the number : "))
def sum_digits(a):
	sum=0
	while a>0:
		b=a%10
		sum=sum+b
		a=a//10
	return(sum)
print(sum_digits(a))