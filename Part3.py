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
        global noError
        if value < 1:
            print("ERROR: Value entered is too low, please try again with a value of one or higher!\n")
            noError = False
        if self.__quantity + value > 100:
            print("ERROR: Cannot have stock over 100 for this item!\n")
            noError = False
        else:
            self.__quantity = self.__quantity + value

    def sellStock(self,value):
        global noError
        if value < 1:
            print("ERROR: Cannot sell less than one of an item!\n")
            noError = False
        elif value > self.__quantity:
            print("ERROR: Cannot sell more stock than is available!\n")
            noError = False
        else:
            self.__quantity = self.__quantity - value

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

# Creating instances of the sub classes
navsys = NavSys("NS101", 10, 99.99, "TomTom")
speaker = Speaker("TS670",  50, 29.99, "Pioneer")
airFreshener = AirFreshener("AF202", 200, 1.50, "Little Trees")
handsFree = HandsFree("HF100", 25, 59.99, "Scosche")

runProgram = True 

itemsInStock = [navsys, speaker, airFreshener, handsFree]

while runProgram: 

    for stockitem in (navsys, speaker, airFreshener, handsFree):
        print(stockitem)

    secondLoop = True
    while secondLoop:  
        stockItemInput = int(input("Which stock item would you like to interact with? (1,2,3,4): "))

        if stockItemInput <= 4:
            break
        else:
            print("This is not a valid option!")
            continue 

    stockItemInput -= 1

    print(itemsInStock[stockItemInput])

    print("MENU")
    print("[1] Set Quantity")
    print("[2] Set Price")
    print("[3] Increase Stock")
    print("[4] Sell Stock")
    

    thirdLoop = True
    while thirdLoop:
        userActionInput = int(input("What would you like to do to this stockitem?: "))

        if userActionInput == 1:
            newQuantity = int(input("What would you like to set the quantity to?: "))
            itemsInStock[stockItemInput].setQuantity(newQuantity)
            break

        elif userActionInput == 2:
            newPrice = int(input("What would you like to set the new price as?: "))
            itemsInStock[stockItemInput].setPrice(newPrice)
            break

        elif userActionInput == 3:
            userIncreaseStock = int(input("How much would you like to increase the stock by?: "))
            itemsInStock[stockItemInput].increaseStock(userIncreaseStock)
            break

        elif userActionInput == 4:
            userSellStock = int(input("How much stock would you like to sell?: "))
            itemsInStock[stockItemInput].sellStock(userSellStock)
            break

        else:
            print("This is not a valid option!")
            continue

    if noError == True:
        print("Here is the updated stock item!")
        print(itemsInStock[stockItemInput])
    
    userInput = input("Would you like to run the program again? (Yes / No)?: ")

    if userInput.upper() == "NO":
        runProgram = False
    
    elif userInput.upper() == "YES":
        continue






        