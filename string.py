a=list(input("\n Enter the string\n").lower())
for i in range(1,len(a)):
     if(a[i]==a[0]):
          a[i]='$'
print(a)