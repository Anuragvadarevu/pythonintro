
class  cars:
	def __init__(self):
		self.brand=''
		self.price=0
	
	def setbrands(self,brand):
		self.brand=brand
		
		
	def setprice(self,price):
		self.price=price
		
		
	def getprice(self):
		return self.price
		
	def getbrands(self):
		return self.brand
		
		
	
carsobj= cars()
carsobj1= cars()
priceobj= cars()
priceobj1= cars()
carsobj.setbrands('honda')
carsobj1.setbrands('BMW')
priceobj.setprice(21000)
priceobj1.setprice(35000)
print(carsobj.getbrands(),priceobj.getprice())
print(carsobj1.getbrands(),priceobj1.getprice())
