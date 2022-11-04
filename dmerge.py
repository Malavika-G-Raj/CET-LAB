d1={}
d2={}
d3={}
a=int(input("Enter no of items in dictionary\n"))
b=int(input("Enter no of items in dictionary\n"))
for i in range(a):
   key=input("Enter key")
   value=input("Enter value")
   d1[key]=value
print(d1)
for j in range(b):
   key=input("Enter key")
   value=input("Enter value")
   d2[key]=value
print(d2)
"""print("\n After Merge\n")
d1.update(d2)
print(d1)"""
d3={**d1,**d2}
for k,v in d3.items():
    if k in d1 and k in d2:
         d3[k]=[v,d1[k]]
print(d3)
