class rectangle:
	def __init__(self,l,w):
		self.__l=l
		self.__w=w
	def area(self):
		self.a=self.__l*self.__w
	def __lt__(self,ob):
		if self.a<ob.a:
			print("Area of 1 st rectangle is greater")
		else:
			print("Area of second rectangle is greater")
a=int(input("Enter the length"))
b=int(input("Enter the width"))			
ob1=rectangle(a,b)
p=int(input("Enter the length"))
q=int(input("Enter the length"))
ob2=rectangle(p,q)
ob1.area()
ob2.area()
ob1<ob2
