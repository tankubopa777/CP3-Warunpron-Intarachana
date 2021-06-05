class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " +self.name+ " " + self.lastName + "'s cart")

customer1 = Customer()
customer1.name = "Bob"
customer1.lastName = "Baby"
customer1.age = 8

customer2 = Customer()
customer2.name = "City"
customer2.lastName = "Pangbuddy"
customer2.age = 18

customer3 = Customer()
customer3.name = "Nat"
customer3.lastName = "Na Nakron"
customer3.age = 18

customer4 = Customer()
customer4.name = "Max"
customer4.lastName = "Duangta"
customer4.age = 19

customer1.addCart()
customer2.addCart()
customer3.addCart()
customer4.addCart()
