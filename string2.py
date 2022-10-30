a=list(input("\n Enter the string\n"))
b=list(input("\nEnter the string 2\n"))
t=a[0]
a[0]=b[0]
b[0]=t
c=a+b
print(c)