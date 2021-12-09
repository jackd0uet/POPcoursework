#A program to keep track of stock items and prices in a car accessories shop.
#PoP Coursework.
#Jack Douet


#Create StockItem Class

class StockItem():

    stockCategory = 'Car accessories'

    def __init__(self, stockCode = 0, quantity = 0, price = 0.0):

        self.stockCode = stockCode
        self.quantity = quantity
        self.price = price

    def getStockCode(self):
        print("The stock code of this item is: %d" %(self.stockCode))

    def getQuantity(self):
        print("The quantity of this item is: %d" %(self.quantity))

    def setQuantity(self,value):
        self.quantity = value

    def getPriceNoVAT(self):
        print("The price of this item without VAT is: %d" %(self.price))

    def setPrice(self,value):
        self.price = value

    def getStockName(self):
        print("Unknown stock name.")

    def getStockDescription(self):
        print("Unknown stock description.")

    def increaseStock(self,value):
        if value < 1:
            print("ERROR: Value entered is too low, please try again with a value of one or higher.")
        if self.quantity + value > 100:
            print("ERROR: Cannot have stock over 100 for this item.")
        else:
            self.quantity = self.quantity + value

    def sellStock(self,value):
        if value < 1:
            print("ERROR: Cannot sell less than one of an item.")
        if value <= self.quantity:
            self.quantity = self.quantity - value
            print("True")
        else:
            print("False")

    def getVAT(self):
        print("17.5")

    def getPriceWithVAT(self):
        print("The price of this item with VAT is: %.2f" % (self.price +(0.175 * self.price)))
        
    def __str__(self):
        #add stock_name and stock_description once defined
        return self.stockCode, self.quantity, self.price

item1 = StockItem(999, 50, 6.0)

print(item1.__str__())





        