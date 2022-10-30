a=int(input("\n Enter the number\n"))
b=int(input("\n Enter 2nd number\n"))
f=1
for i in range(1,a):
    for j in range(1,b):
      if(a%i==0 and b%j==0):
         if(i==j):
             f=f*i
print("GCD is",f)
