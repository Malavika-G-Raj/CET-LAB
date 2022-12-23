class Time:
	def __init__(self,hr,mi,sec):
		self.__hr=hr
		self.__mi=mi
		self.__sec=sec
	def __add__(self,ob):
		self.__hr+=ob.__hr
		self.__mi+=ob.__mi
		self.__sec+=ob.__sec
		while(self.__mi>60 or self.__sec>60):
			if self.__mi>60:
				self.__hr+=int(self.__mi//60)
				self.__mi=self.__mi%60
			if(self.__sec>60):
				self.__mi+=int(self.__sec//60)
				self.__sec=self.__sec%60
	def display(self):
		print("Time=",self.__hr,"Hours",self.__mi,"Minutes",self.__sec,"Seconds")
a=int(input("Enter the Hour"))
b=int(input("Enter the minute"))
c=int(input("Enter the seconds"))
ob1=Time(a,b,c)
ob1.display()
p=int(input("Enter the Hour"))
q=int(input("Enter the minute"))
r=int(input("Enter the seconds"))
ob2=Time(p,q,r)
ob2.display()
ob1+ob2
ob1.display()
