a=list(input("\nEnter the list\n").split(" "))
print(a)
for i in range(len(a)):
	if int(a[i])>100:
		a[i]='over'
print(a)

"""b=[]
for x in a:
    if x>100:
        y='over'
        b.append(y)
    else:
        b.append(x)
print(b)"""
