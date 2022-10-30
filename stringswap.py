a=list(input("\nEnter the string\n"))
t=a[0]
a[0]=a[len(a)-1]
a[len(a)-1]=t
print(a)