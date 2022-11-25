def ing(a):
    l=len(a)
    str=a[l-3]+a[l-2]+a[l-1]
    if str=='ing':
         a=a+'ly'
    else:
         a=a+'ing'
    print(a)
c=input("\n Enterthe string:")
ing(c)
