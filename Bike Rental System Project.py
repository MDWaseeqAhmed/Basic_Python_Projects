# BIKE RENTAL SYSTEM
print("BIKE RENTAL SYSTEM") # Should be in Bold letters
print( )

class Bike_Shop:
    def __init__(self,stock):
        self.stock=stock
    def displaybike(self):
        print("Total Bikes",self.stock)
    def rentabike(self,q):
        if q<=0:
            print("Enter the positive value or greater then Zero")
        elif q>self.stock:
            print("Enter the value (less then Stock)")
        else:
            self.stock=self.stock-q
            print("Total Price",q*100)
            print("Total Bikes",self.stock)
while True:
    obj=Bike_Shop(100) # the error showing before was for not adding this line
# this line is most important to define the object for the cod
    uc=int(input('''
1. DISPLAY STOCKS
2. RENT A BIKE
3. EXIT
'''))
    if uc==1:
        obj.displaybike()
    elif uc==2:
        n=int(input("Enter the Qty:- "))
        obj.rentabike(n)
    else:
        break
