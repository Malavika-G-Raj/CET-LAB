def sum(a):
    sum=0
    for i in a:
       sum=sum+i
    print("The sum is:",sum)
l1=list(map(int,input("Enter the list ").split()))
sum(l1)


