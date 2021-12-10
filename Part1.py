#A program to keep track of stock items and prices in a car accessories shop.
#PoP Coursework.
#Jack Douet


#Create StockItem Class

class StockItem():

    stockCategory = 'Car accessories'

    def __init__(self, stockCode = 0, quantity = 0, price = 0.0):

        self.__stockCode = stockCode
        self.__quantity = quantity
        self.__price = price

    def getStockCode(self):
        return self.__stockCode

    def getQuantity(self):
        return self.__quantity

    def setQuantity(self,value):
        self.__quantity = value

    def getPriceNoVAT(self):
        return self.__price

    def setPrice(self,value):
        self.__price = value

    def getStockName(self):
        return "Unknown stock name."

    def getStockDescription(self):
        return "Unknown stock description."

    def increaseStock(self,value):
        if value < 1:
            print("ERROR: Value entered is too low, please try again with a value of one or higher.")
        if self.__quantity + value > 100:
            print("ERROR: Cannot have stock over 100 for this item.")
        else:
            self.__quantity = self.__quantity + value

    def sellStock(self,value):
        if value < 1:
            print("ERROR: Cannot sell less than one of an item.")
        if value <= self.__quantity:
            self.__quantity = self.__quantity - value
            return "True"
        else:
            return "False"

    def getVAT(self):
        return "17.5"

    def getPriceWithVAT(self):
        x = self.__price +(0.175 * self.__price)
        x = round(x, 2)
        return x
        
    def __str__(self):
        #add stock_name and stock_description once defined
        return "\nPrinting item stock information: " "\nStock Category: " + self.stockCategory + "\nStock Type: " + self.getStockName() + "\nDescription: " + self.getStockDescription() + "\nStockCode: " + str(self.getStockCode()) + "\nPriceWithoutVat: " +str(self.getPriceNoVAT()) + "\nPriceWithVat: " +str(self.getPriceWithVAT()) + "\nTotal units in stock: " +str(self.getQuantity()) + "\n"





print("Creating a stock with 10 units Unknown item, price 99.99 each, and item code W101")
item1 = StockItem("W101", 10, 99.99)

print(item1)

print("Increasing 10 more units")
item1.increaseStock(10)
print(item1)

print("Sold 2 items")
item1.sellStock(2)
print(item1)

print("Set new price 100.99 per unit")
item1.setPrice(100.99)
print(item1)

print("Increasing 0 more units")
item1.increaseStock(0)





        