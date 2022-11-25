def  char(a):
    b={}
    for i in a:
        if i in b:
            b[i]+=1
        else:
            b[i]=1
    print("The count of all character are:", b)
l1=list(input("\n Enter the string:"))
char(l1)
