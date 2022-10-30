a=list(input("Enter a statement\n").split(" "))
c=[]
for x in a:
    b=0
    for y in a:
       if(x==y):
        b+=1
    c.append(b)
print(c)