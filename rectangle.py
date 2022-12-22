class rectangle:
  def __init__(self,l,b):
	self.l=l
	self.b=b
  def area(self):
        a=self.l*self.b
	print("Area:",a)	
  def peri(self):
        p=2*(self.l+self.b)
        print("Perimeter=",p)
  def comp(self,ob):
        if self.a==ob.a:
	   print("Same area")
        else:
	   print("Different area")
ob1=rectangle(23,45)
ob2=rectangle(34,67)
ob1.area()
ob2.area()
ob1.peri()
ob2.peri()
ob1.comp(ob2)
