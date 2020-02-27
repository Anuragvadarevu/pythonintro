from cars import cars

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


