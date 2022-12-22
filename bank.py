class Bank:
	def __init__(self,ano,name,typ):
		self.ano=ano
		self.name=name
		self.typ=typ
		self.bal=0
	def deposit(self):
		m=int(input("Enter the amount to be deposited:"))
		self.bal=self.bal+m
		print("Deposited successfully.Balence=",self.bal)
	def withdraw(self):
		n=int(input("Enter the amount to  withdraw:"))
		if n>self.bal:
			print("Withdrawal not possible")
		else:
			self.bal=self.bal-n
			print("Withdrawal successfull.Balence=",self.bal)
	def menu(self):
		print("1.Deposite")
		print("2.Withdraw")
		print("3.Exit")
		n=int(input("Enter your choice"))
		return n
	
no=input("Enter account number")
name=input("Enter name:")
typ=input("Enter type:")
ob1=Bank(no,name,typ)
ch=ob1.menu()
while(ch<4):
	if(ch==1):
		ob1.deposit()
		ch=ob1.menu()
	elif(ch==2):
		ob1.withdraw()
		ch=ob1.menu()
	elif(ch==3):
		exit()

		
