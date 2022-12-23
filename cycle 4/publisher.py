class publisher:
	def __init__(self,name):
		self.name=name
class book(publisher):
	def __init__(self,n,t,a):
		publisher.__init__(self,n)
		self.title=t
		self.author=a
	def display(self):
		print("Title=",self.title,"\nAuthor=",self.author)
					
class python(book):
	def __init__(self,n,t,a,p,pag):
		book.__init__(self,n,t,a)
		self.price=p
		self.page=pag
	def display(self):
		print("\nName=",self.name,"\n Title:",self.title,"\n author:",self.author,"\n price=",self.price,"\n no.of page=",self.page)
ob=python("Rupa publications","Three Mistakes Of My Life","Chetan Bhagath","300","390")
ob.display()

