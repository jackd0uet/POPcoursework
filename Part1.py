#A program to keep track of stock items and prices in a car accessories shop.
#PoP Coursework.
#Jack Douet


#Create StockItem Class

class StockItem():

    stock_category = 'Car accessories'

    def __init__(self, stock_code = 0, quantity = 0, price = 0.0):

        self.stock_code = stock_code
        self.quantity = quantity
        self.price = price

    def get_stock_code(self):
        print("The stock code of this item is: %d" %(self.stock_code))

    def get_quantity(self):
        print("The quantity of this item is: %d" %(self.quantity))

    def set_quantity(self,value):
        self.quantity = value

    def get_price_no_VAT(self):
        print("The price of this item without VAT is: %d" %(self.price))

    def set_price(self,value):
        self.price = value

    def get_stock_name(self):
        print("Unknown stock name.")

    def get_stock_description(self):
        print("Unknown stock description.")

    def increase_stock(self,value):
        if value < 1:
            print("ERROR: Value entered is too low, please try again with a value of one or higher.")
        if self.quantity + value > 100:
            print("ERROR: Cannot have stock over 100 for this item.")
        else:
            self.quantity = self.quantity + value

    def sell_stock(self,value):
        if value < 1:
            print("ERROR: Cannot sell less than one of an item.")
        if value <= self.quantity:
            self.quantity = self.quantity - value
            print("True")
        else:
            print("False")

    def get_VAT(self):
        print("17.5")

    def get_price_with_VAT(self):
        print("The price of this item with VAT is: %.2f" % (self.price +(0.175 * self.price)))
        
    def __str__(self):
        #add stock_name and stock_description once defined
        return self.stock_code, self.quantity, self.price

item1 = StockItem(999, 50, 6.0)

print(item1.__str__())





        