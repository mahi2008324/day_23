a=list(input("enter list 1 elements : "))
b=list(input("enter list 2 elements : "))
c=set(a)
d=set(b)
e=c&d
f=list(e)
print(a)
print(b)
print("common elements",f)