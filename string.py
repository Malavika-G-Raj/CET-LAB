a=list(input("\n Enter the string\n").lower())
B=a[0]
C=B+" "
for i in range(1,len(a)):
     if(a[i]==a[0]):
          a[i]='$'
     C+=a[i]
print(C)
