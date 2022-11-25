def lent(a):
    long=0
    for i in a:
        if len(i) > long:
            long=len(i)
            c=i
    print(c,"is the longest word of length",long)
    
l1=list(input("\n Enter the words:\n").split())
lent(l1)
