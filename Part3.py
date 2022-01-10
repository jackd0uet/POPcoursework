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

class Speaker(StockItem):
    def __init__(self, stockCode, quantity, price, speakerBrand):
        self.__speakerBrand = speakerBrand
        super().__init__(stockCode,quantity,price)

    def getStockName(self):
        return "Speaker"

    def getStockDescription(self):
        return "Surround Sound"

    def __str__(self):
        return super().__str__() + "Brand: " + self.__speakerBrand + "\n"

class AirFreshener(StockItem):
    def __init__(self, stockCode, quantity, price, airFreshenerBrand):
        self.__airFreshenerBrand = airFreshenerBrand
        super().__init__(stockCode, quantity, price)

    def getStockName(self):
        return "Air Freshener"

    def getStockDescription(self):
        return "Minty fresh!"

    def __str__(self):
        return super().__str__() +"Brand: " + self.__airFreshenerBrand + "\n"

class HandsFree(StockItem):
    def __init__(self, stockCode, quantity, price, handsFreeBrand):
        self.__handsFreeBrand = handsFreeBrand
        super().__init__(stockCode, quantity, price)

    def getStockName(self):
        return "Hands Free"

    def getStockDescription(self):
        return "Look ma no hands!"

    def __str__(self):
        return super().__str__() +"Brand: " + self.__handsFreeBrand + "\n"

runProgram = True   
while runProgram: 
    # Creating instances of the sub classes
    navsys = NavSys(99.99, 10, "NS101", "TomTom")
    speaker = Speaker(29.99, 50, "TS670", "Pioneer")
    airFreshener = AirFreshener(1.50, 200, "AF202", "Little Trees")
    handsFree = HandsFree(59.99, 25, "HF100", "Scosche")

    userInput = input("Would you like to run the program again? (Yes / No)?: ")

    if userInput.upper() == "NO":
        runProgram = False
    
    elif userInput.upper() == "YES":
        print ("wwwww")

# print("Creating a stock with 10 units Navigation system, price 99.99 each, item code NS101, and brand TomTom")
# nav = NavSys("NS101", 10, 99.99, "TomTom")
# print(nav)

# nav.increaseStock(10)
# print(nav)

# nav.sellStock(2)
# print(nav)

# nav.setPrice(100.99)
# print(nav)

# nav.increaseStock(0)







        