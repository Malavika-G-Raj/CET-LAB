def pyramid(n):
  for i in range(0,n):
     f=""
     for j in range(0,i+1):
        f+="*"+" "
     print(f)
     print("")
  for k in range(n-1,0,-1):
     r=""
     for p in range(1,k+1):
        r+="*"+" "
     print(r)
     print()
a=int(input("\n Enter the row:\n"))
pyramid(a)