a=[]
b=[]
n=int(input("size of a"))
m=int(input("Size of b"))
for i in range(1,n+1):
      c=input("Enter the element of a")
      a.append(c)
for i in range(1,m+1):
      d=input("Enter the element of b")
      b.append(d)
print("List 1:",a)
print("List 2:",b)
print("Check whether the two list are of same length:\n")
if(n==m):
       print("The list are of same length\n")
else:
       print("The list are of different length\n")

print("Check weather the list are identical:\n")
a.sort()
b.sort()
if(a==b):
        print("The lists ae identical\n")
else:
        print("The list are not identical\n")

print("Check weather elements occur in both lists:\n")
c=[]
for x in a:
     for y in b:
            if(x==y):
             c.append(x)
if(len(c)>0):       
       print("The value",c,"Occur in both list\n")
else:
       print("No similar values occur in both lists\n")