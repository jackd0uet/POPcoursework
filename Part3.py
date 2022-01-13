# A program to keep track of stock items and prices in a car accessories shop.
# PoP Coursework.
# Jack Douet


# Create StockItem Class
class StockItem():

    # Create class variable for default stock category.
    stockCategory = 'Car accessories'

    # Define constructor variable for base class.
    def __init__(self, stockCode, quantity, price):

        # Create private variables for stockcode, quantity and price.
        self.__stockCode = stockCode
        self.__quantity = quantity
        self.__price = price

    # Define appropriate setters and getters for stockcode, quantity, price with and without VAT, stock name and description.
    def getStockCode(self):
        return self.__stockCode

    def getQuantity(self):
        return self.__quantity

    def setQuantity(self, quantity):
        self.__quantity = quantity

    def getPriceNoVAT(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price

    def getStockName(self):
        return "Unknown stock name."

    def getStockDescription(self):
        return "Unknown stock description."

    def getVAT(self):
        return "17.5"

    # Define a function for calculating the price of the object with the VAT rate that has been entered above.
    def getPriceWithVAT(self):
        x = self.__price + (0.175 * self.__price)
        x = round(x, 2)
        return x

    # Define function for increasing the amount of stock for an individual object of the class.

    def increaseStock(self, stock):
        # Create a global noError variable for use later in the program for better user experience.
        global noError
        # Use if statements to check whether the value entered is valid and print an error if it is not.
        if stock < 1:
            print(
                "ERROR: Value entered is too low, please try again with a value of one or higher!\n")
            # Set noError to false if the value entered is invalid.
            noError = False

        elif self.__quantity + stock > 100:
            print("ERROR: Cannot have stock over 100 for this item!\n")
            # Set noError to false if the value entered is invalid.
            noError = False

        # Otherwise set the quantity to the original quantity plus the user's entered value.
        else:
            self.__quantity = self.__quantity + stock

    # Define function for selling stock for an individual object of the class.

    def sellStock(self, stock):
        # Again define the global variable so that it can be accessed from outside this function creation.
        global noError
        # Use if statements to check whether the value entered is valid and print an error if it is not.
        if stock < 1:
            print("ERROR: Cannot sell less than one of an item!\n")
            # Set noError to false if the value entered is invalid.
            noError = False

        elif stock > self.__quantity:
            print("ERROR: Cannot sell more stock than is available!\n")
            # Set noError to false if the value entered is invalid.
            noError = False

        # Otherwise set the quantity of the object to the original quantity minus the user's entered value.
        else:
            self.__quantity = self.__quantity - stock

    # Define string method so when the print function is called on an object of this class a formatted string will be printed.
    def __str__(self):
        return "\nPrinting item stock information: " "\nStock Category: " + self.stockCategory + "\nStock Type: " + self.getStockName() + "\nDescription: " + self.getStockDescription() + "\nStockCode: " + str(self.getStockCode()) + "\nPriceWithoutVat: " + str(self.getPriceNoVAT()) + "\nPriceWithVat: " + str(self.getPriceWithVAT()) + "\nTotal units in stock: " + str(self.getQuantity()) + "\n"


# Define a new class that inherits from the StockItem parent class.
class NavSys(StockItem):
    # Inherit stockCode, quantity and price from the StockItem parent and create a new variable indicating a new class of item.
    def __init__(self, stockCode, quantity, price, navSysBrand):
        self.__navSysBrand = navSysBrand
        super().__init__(stockCode, quantity, price)

    # Replace the default stockName with Navigation System.
    def getStockName(self):
        return "Navigation System"

    # Replace the default stockDescription with Geovision Sat Nav.
    def getStockDescription(self):
        return "GeoVision Sat Nav"

    # Inherit the string method from parent class and add the brand to the end.
    def __str__(self):
        return super().__str__() + "Brand: " + self.__navSysBrand + "\n"


# Define another new class that inherits from the StockItem parent class.
class Speaker(StockItem):
    # Inherit stockCode, quantity and price from the StockItem parent and create a new variable indicating a new class of item.
    def __init__(self, stockCode, quantity, price, speakerBrand):
        self.__speakerBrand = speakerBrand
        super().__init__(stockCode, quantity, price)

    # Replace the default stockName with Speaker.
    def getStockName(self):
        return "Speaker"

    # Replace the default stockDescription with Surround Sound.
    def getStockDescription(self):
        return "Surround Sound"

    # Inherit the string method from parent class and add the brand to the end.
    def __str__(self):
        return super().__str__() + "Brand: " + self.__speakerBrand + "\n"


# Define another new class that inherits from the StockItem parent class.
class AirFreshener(StockItem):
    # Inherit stockCode, quantity and price from the StockItem parent and create a new variable indicating a new class of item.
    def __init__(self, stockCode, quantity, price, airFreshenerBrand):
        self.__airFreshenerBrand = airFreshenerBrand
        super().__init__(stockCode, quantity, price)

    # Replace the default stockName with Air Freshener.
    def getStockName(self):
        return "Air Freshener"

    # Replace the default stockDescription with Minty Fresh!
    def getStockDescription(self):
        return "Minty fresh!"

    # Inherit the string method from parent class and add the brand to the end.
    def __str__(self):
        return super().__str__() + "Brand: " + self.__airFreshenerBrand + "\n"


# Define another new class that inherits from the StockItem parent class.
class HandsFree(StockItem):
    # Inherit stockCode, quantity and price from the StockItem parent and create a new variable indicating a new class of item.
    def __init__(self, stockCode, quantity, price, handsFreeBrand):
        self.__handsFreeBrand = handsFreeBrand
        super().__init__(stockCode, quantity, price)

    # Replace the default stockName with Hands Free.
    def getStockName(self):
        return "Hands Free"

    # Replace the default stockDescription with Look ma no hands!
    def getStockDescription(self):
        return "Look ma no hands!"

    # Inherit the string method from parent class and add the brand to the end.
    def __str__(self):
        return super().__str__() + "Brand: " + self.__handsFreeBrand + "\n"


# Define main function.
def main():
    # Creating instances of the sub classes
    navsys = NavSys("NS101", 10, 99.99, "TomTom")
    speaker = Speaker("TS670",  50, 29.99, "Pioneer")
    airFreshener = AirFreshener("AF202", 200, 1.50, "Little Trees")
    handsFree = HandsFree("HF100", 25, 59.99, "Scosche")

    # Create array to store created objects.
    itemsInStock = [navsys, speaker, airFreshener, handsFree]

    # Create a variable and set to true for use with a while loop.
    runProgram = True

    # While loop for user interface.
    while runProgram:

        # For loop to show all of the available objects.
        for stockitem in (navsys, speaker, airFreshener, handsFree):
            print(stockitem)

        # Create a variable and set to true for use with a while loop.
        userSelectionLoop = True
        # While loop to ask user which object they would like to interact with.
        while userSelectionLoop:
            # Capture the input as integer in a variable.
            stockItemInput = int(
                input("Which stock item would you like to interact with? : "))
            # If the user inputs a number that is within the length of the itemsInStock array and is not zero break out of the while loop.
            if stockItemInput <= len(itemsInStock) and stockItemInput != 0:
                break
            # If the user enters anything else, print an error and continue to the top of the loop.
            else:
                print("ERROR: This is not a valid option!")
                continue

        # Take one of the users entered input so that it correctly matches up with the index in the array for that object.
        stockItemInput -= 1

        # Print out the users selected object from the array of objects.
        print(itemsInStock[stockItemInput])

        # Print out a menu of functions that can be done to the object.
        print("MENU")
        print("[1] Set Quantity")
        print("[2] Set Price")
        print("[3] Increase Stock")
        print("[4] Sell Stock")

        # Variable for initialising a while loop for the user menu.
        functionLoop = True
        # While loop for picking option from printed menu.
        while functionLoop:
            # Set noError to true in case it is set to false by an incorrect increase or sell of stock.
            noError = True
            # Ask user what they would like to do and capture their input.
            userActionInput = int(
                input("What would you like to do to this stockitem?: "))
            # If user picks option 1, run function for setting quantity.
            if userActionInput == 1 and userActionInput != 0:
                # Ask the user what they would like to set the quantity as and capture as an integer.
                newQuantity = int(
                    input("What would you like to set the quantity to?: "))
                # Set the quantity to entered integer and break out of loop.
                itemsInStock[stockItemInput].setQuantity(newQuantity)
                break
            # If user picks option 2, run function for setting price.
            elif userActionInput == 2 and userActionInput != 0:
                # Ask the user what they would like to set the price to and capture as a double.
                newPrice = float(
                    input("What would you like to set the new price as?: "))
                # Set the quantity to entered double and break out of loop.
                itemsInStock[stockItemInput].setPrice(newPrice)
                break
            # If user picks option 3, run function for increasing stock.
            elif userActionInput == 3 and userActionInput != 0:
                # Ask the user how much they would like to increase the stock by and capture as int.
                userIncreaseStock = int(
                    input("How much would you like to increase the stock by?: "))
                # Use the entered int in the function to increase the stock and break out of loop.
                itemsInStock[stockItemInput].increaseStock(userIncreaseStock)
                break
            # If user picks option 4, run function for selling stock.
            elif userActionInput == 4 and userActionInput != 0:
                # Ask the user how much stock they would like to sell and capture as int.
                userSellStock = int(
                    input("How much stock would you like to sell?: "))
                # Use the entered int in the function to sell the stock and break out of loop.
                itemsInStock[stockItemInput].sellStock(userSellStock)
                break
            # Otherwise warn the user that they have entered an invalid option and continue to the top of the loop.
            else:
                print("ERROR: This is not a valid option!")
                continue

        # If there has been no error in the user's query print the updated object.
        if noError == True:
            print("Here is the updated stock item!")
            print(itemsInStock[stockItemInput])

        # Variable for initialising while loop.
        askUser = True
        # While loop for asking the user if they would like to run the program again.
        while askUser:
            userInput = input(
                "Would you like to run the program again? (Yes / No)?: ")
            # Use .upper to capitalise the input.
            userInput = userInput.upper()
        # If the user says no, break out of the loop.
            if userInput == "NO":
                runProgram = False
                break
        # If the user says yes, carry on the loop.
            elif userInput == "YES":
                break
            else:
                print("ERROR: This is not a valid option!")
                continue


if __name__ == "__main__":
    main()
