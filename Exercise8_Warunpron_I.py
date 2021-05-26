username = input("Username :")
password = input("Password :")
if username == "Tankub" and password == "12345":
    print("Success")
    print("Welcome to Tankubopa shop")
    print("-------------------------")
    print("Goods list")
    print("1.Coffee      1x : 45 THB")
    print("2.Milk        1x : 15 THB")
    print("3.Americano   1x : 45 THB")
    print("4.Cappuccino  1x : 45 THB")
    print("5.Cafe Latte  1x : 45 THB")
    print("6.Water       1x : 10 THB")
    print("-------------------------")
    print("Choose number of drinks to order")
    Goods = int(input("Order :"))
    if Goods == 1 :
        print("You just choose Coffee")
        print("How many you want for coffee?")
        y = int(input("Number of coffee :"))
        y *= 45
        print("Price :",y,"THB")
    elif Goods == 2 :
        print("You just choose Milk")
        print("How many you want for milk?")
        y = int(input("Number of milk :"))
        y *= 15
        print("Price :", y, "THB")
    elif Goods == 3 :
        print("You just choose Americano ")
        print("How many you want for americano?")
        y = int(input("Number of americano :"))
        y *= 45
        print("Price :", y, "THB")
    elif Goods == 4 :
        print("You just choose Cappuccino")
        print("How many you want for cappuccino?")
        y = int(input("Number of cappuccino :"))
        y *= 45
        print("Price :", y, "THB")
    elif Goods == 5 :
        print("You just choose Cafe Latte")
        print("How many you want for cafe latte?")
        y = int(input("Number of Cafe Latte:"))
        y *= 45
        print("Price :", y, "THB")
    elif Goods == 6 :
        print("You just choose Water")
        print("How many you want for water?")
        y = int(input("Number of water:"))
        y *= 10
        print("Price :", y, "THB")
    print("Thank you")
else :
    print("Not found")
