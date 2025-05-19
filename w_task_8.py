a=int(input("Enter the number : "))
def sum_digits(a):
	sum=0
	while a>0:
		b=a%10
		sum=sum+b
		a=a//10
	print(sum)
sum_digits(a)