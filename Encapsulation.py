
class BankAccount:

    def __init__(self, owner, balance):
        self.owner =  owner
        self.__balance = balance 

    def get_balance(self):
        return self.__balance
    def deposite(self, amount):
        if amount>0:
            self.__balance += amount
        else:
            print("Invalid deposite amount!")

my_account = anniksi = BankAccount("Alice",1000)
my_account.deposite(500)
my_account.deposite(690)

print(my_account.get_balance()) 




# About students:

class student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if 0<age<120:
            self.__age = age
        else:
            print("Error:Age must be b/w 1 and 119")    
student = student("Rajesh",23)
print(student.get_name())
student.set_age(25)
print(student.get_age())  
student.set_age(150)

# The smart phone battery level:

class smartphone:
    def __init__(self, brand, battery_level):
        self.__brand = brand
        self.__battery_level = battery_level
    def get_brand(self):
        return self.__brand
    def get_battery_level(self):
        return f"{self.__battery_level}%"
    def charge(self, amount):
        if amount>0:
            self.__battery_level += amount
            if self.__battery_level>100:
                self.__battery_level = 100
            print(f"charged! current battery is{self.__battery_level}%")
        else:
            print("Invalid charge amount")

myphone = smartphone("Google Pixel",40)
print(myphone.get_brand())
print(myphone.get_battery_level())
myphone.charge(50)         
 
#myphone1 = smartphone("Apple",68)
#print(myphone1.get_brand())
#print(myphone1.get_battery_level())
#myphone1.charge(30) 


# Paradise movie, Booking tickets process:
class MovieTheater:
    def __init__(self,Movietitle,Available_seats):
        self.__Movietitle = Movietitle
        self.__Available_seats = Available_seats
    def get_Movietitle(self):
        return self.__Movietitle
    def get_Available_seats(self):
        return self.__Available_seats
    def Booking_Tickets(self,count):
        if count<=0:
            print("Please enter an invalidnumber")
        elif count >self.__Available_seats:
            print("Sorry you don't have enough seats")
        else:
            self.__Available_seats -= count
            print(f"Successfully your {count} tickets are booked, Enjoy the movie! ")
Sandhya_Theater = MovieTheater("Paradise",25)
print(Sandhya_Theater.get_Movietitle())
print(Sandhya_Theater.get_Available_seats())
Sandhya_Theater.Booking_Tickets(15) 
