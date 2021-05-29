def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "Tankub" and passwordInput == "12345":
        return True
    else:
        return False
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    return userSelected
def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

if(login())==True:
    showMenu()
    x = menuSelect()
    if x == 1 :
        totalPrice = int(input("กรุณาใส่ราคาสินค้า :"))
        print(vatCalculator(totalPrice))
    elif x == 2 :
        totalPrice = priceCalculator()
        (vatCalculator(totalPrice))
        print((vatCalculator(totalPrice)))