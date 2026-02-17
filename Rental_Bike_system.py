class bikeShop:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("Total Bikes",self.stock)
    def rentForBike(self,Quantity):
        if Quantity<=0:
            print("Enter the positive value OR Greater then 0")
        elif Quantity>self.stock:
            print("Enter the value (Less then stock)")
            print(bikeShop)
        else:
            self.stock=self.stock-Quantity
            print("Total Prices", Quantity*100)
            print("Total Bikes", self.stock)

while True:
    obj=bikeShop(100)
    uc=int(input('''
1. Display Stock
2. Rent a bike
3. Exit 
    '''
    ))

    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Enter The Quantity:--"))
        obj.rentForBike(n)
    else:
        break