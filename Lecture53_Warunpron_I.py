def Vat(Price):
    x = Price*107/100
    return x
Price = int(input("กรุณาใส่ราคา :"))
Vat(Price)
print(Vat(Price))
