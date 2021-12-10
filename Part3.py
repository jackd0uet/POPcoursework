#A program to keep track of stock items and prices in a car accessories shop.
#PoP Coursework.
#Jack Douet


#Create StockItem Class

class StockItem():

    stockCategory = 'Car accessories'

    def __init__(self, stockCode, quantity, price):

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
        return "\nPrinting item stock information: " "\nStock Category: " + self.stockCategory + "\nStock Type: " + self.getStockName() + "\nDescription: " + self.getStockDescription() + "\nStockCode: " + str(self.getStockCode()) + "\nPriceWithoutVat: " +str(self.getPriceNoVAT()) + "\nPriceWithVat: " +str(self.getPriceWithVAT()) + "\nTotal units in stock: " +str(self.getQuantity()) + "\n"


class NavSys(StockItem):
    def __init__(self,stockCode, quantity, price, navSysBrand):
        self.__navSysBrand = navSysBrand
        super().__init__(stockCode, quantity, price)

    def getStockName(self):
        return "Navigation System"

    def getStockDescription(self):
        return "GeoVision Sat Nav"

    def __str__(self):
        return super().__str__() + "Brand: " + self.__navSysBrand + "\n"

class Tyres(StockItem):
    def __init__(self,stockCode,quantity,price,tyreBrand):
        self.__tyreBrand = tyreBrand
        super().__init__(stockCode,quantity,price)

    def getStockName(self):
        return "Tyre"

    def getStockDescription(self):
        return "All Terrain"

    def __str__(self):
        return super().__str__() + "Brand: " + self.__tyreBrand + "\n"

class AirCon(StockItem):
    def __init__(self, stockCode, quantity, price, airConBrand):
        self.__airConBrand = airConBrand
        super().__init__(stockCode, quantity, price)

    def getStockName(self):
        return "Air Conditioning"

    def getStockDescription(self):
        return "In car air conditioning replacements"

    def __str__(self):
        return super().__str__() +"Brand: " + self.__airConBrand + "\n"

class Windshields(StockItem):
    def __init__(self, stockCode, quantity, price, windshieldBrand):
        self.__windshieldBrand = windshieldBrand
        super().__init__(stockCode, quantity, price)

    def getStockName(self):
        return "Windshield"

    def getStockDescription(self):
        return "Replacement glass"

    def __str__(self):
        return super().__str__() +"Brand: " + self.__windshieldBrand + "\n"

print("Creating a stock with 10 units Navigation system, price 99.99 each, item code NS101, and brand TomTom")
nav = NavSys("NS101", 10, 99.99, "TomTom")
print(nav)

nav.increaseStock(10)
print(nav)

nav.sellStock(2)
print(nav)

nav.setPrice(100.99)
print(nav)

nav.increaseStock(0)







        