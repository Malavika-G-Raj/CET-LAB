c1=list(input("\nEnter the colors\n").split(" "))
c2=list(input("\nEnter the colors\n").split(" "))
c=[]
c=[i for i in c1 if i not in c2]
print(c)