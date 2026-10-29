
# Parent class (Super class):
class vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed 
    def start_engine(self):
        print(f"The {self.brand}'s engine is now running. Vroom!")
    def stop_engine(self):
        print(f"The {self.brand}'s engine has stopped.")         

# Child class (subclass) inheritance from vehicle
class car(vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors
    def open_truck(self):
        print(f"The truck of the {self.brand} car is now open.")

my_car = car("Toyota",180,4)
my_car.start_engine()
my_car.stop_engine()
print(f"Top speed:{my_car.speed} km/h, Doors:{my_car.doors}")
 


#  parent class:
class Employee:
    def __init__(self,Name,Salary):
        self.Name = Name
        self.Salary = Salary 
    def get_details(self):
        return f"Name:{self.Name}\nSalary:${self.Salary}"

# child class:
class chef(Employee):
    def __init__(self,Name,Salary,Speciality):
        super().__init__(Name,Salary)
        self.Speciality = Speciality        
    def cook_food(self):
        return f"{self.Name} is cooking delicious {self.Speciality}"


my_chef = chef("chef Raghava",5000,"French Pastry")
print(my_chef.get_details())   
print(my_chef.cook_food())  

print("===========================================================")
# Child class:
class waiter(Employee):
    def __init__(self,Name,Salary,work):
        super().__init__(Name,Salary)
        self.work = work
    def waiter_duity(self):
        return f"{self.Name} duity is to take upto the initiative of {self.work}"    
Waiter = waiter("Srikanth",3500,"First floor tables")
print(Waiter.get_details())
print(Waiter.waiter_duity())    


# E-Commerce App:
# partent class - "Product"
# Children class - "Book","Electronic Gadget"

# parent class:
class Product:
    def __init__(self,Name,Price):
        self.Name = Name
        self.Price = Price
    def get_details(self):
        return f"Product:{self.Name}\nPrice:${self.Price}"

# Child class1:
class Book(Product):
    def __init__(self,Name,Price,language):
        super().__init__(Name,Price)
        self.language = language 
    def Book_language(self):
        return f"The language of book is:{self.language}"

my_book = Book("Ramayana Book",150,"Telugu")
#my_book = Book("Ramayana Book",150,"Sanskrit")
print(my_book.get_details())
print(my_book.Book_language())       
print("==================================================")
# Child class2:
class Electronic_gadget(Product):
    def __init__(self,Name,Price,Brand,Warranty):
        super().__init__(Name,Price)
        self.Brand = Brand
        self.Warranty = Warranty
    def Gadget(self):
        return f"Warranty:{self.Warranty}years"
Electronic_gadget1 = Electronic_gadget("Smart Watch",125,"Noise_fit",2)
Electronic_gadget2 = Electronic_gadget("Laptop",1250,"Lenovo",2)

print(Electronic_gadget1.get_details())
print(Electronic_gadget1.Gadget())
print(Electronic_gadget2.get_details())
print(Electronic_gadget1.Gadget())


# Mobile Application to control smart home appliances:
# Parent class 

class SmartDevice:
    def __init__(self,Name):
        self.Name = Name
    def get_details(self):
        return f"Name:{self.Name}"
# Child class:
class smart_light(SmartDevice):
    def __init__(self,Name,Charging_level):
        super().__init__(Name)
        self.Charging_level = Charging_level 
    def Power_status(self):
        return f"The power of the {self.Name} is {self.Charging_level}%"     
SmartDevice1 = smart_light("Living Room light",80)      
print(SmartDevice1.get_details())
print(SmartDevice1.Power_status())  




#Parent class:
class Course:
    def __init__(self,Title,Instructor):
        self.Title = Title
        self.Instructor = Instructor 
    def get_details(self):
        return f"Course: {self.Title}\nInstructor: {self.Instructor}"




# Child class:
class Videocourse(Course): 
    def __init__(self,Title,Instructor,price,Time):
        super().__init__(Title,Instructor)
        self.price = price
        self.Time = Time 
    def Paid_Course(self):
        return f"The {self.Title} course was instructed by {self.Instructor}sir\nThe price of the course is {self.price}\nThe videocourse takes {self.Time}-months duration"
Course1 = Videocourse("Python","Ramesh",5000,6) 
print(Course1.Paid_Course())    
print(Course1.get_details())             



# Single Inheritance:
# Parent class:
class Vehicle:
    def __init__(self,Brand,Model):
        self.Brand = Brand
        self.Model = Model
    def start_engine(self):
        return f"The {self.Brand} {self.Model} engine is now running."
# Child class:
class Electriccar(Vehicle):
    def __init__(self,Brand,Model,charge_battery):
        super().__init__(Brand,Model)
        self.charge_battery = charge_battery
    def Battery(self):
        return f"The current battery of the car is {self.charge_battery}%"  

my_car = Electriccar("Benze","Corolla",85)
print(my_car.start_engine())
print(my_car.Battery()) 




# Multilevel Inheritance:
# Grand Parent class:
class Product:
    def __init__(self,Brand,Price):
        self.Brand = Brand
        self.Price = Price 
# Parent class:
class Kurthi(Product):
    def __init__(self,Brand,Price,size):
        super().__init__(Brand,Price)
        self.size = size
    
# Child class:
class Color(Kurthi):
    def __init__(self,Brand,Price,size,dark_colors):
        super().__init__(Brand,Price,size)
        self.dark_colors = dark_colors 
    def get_details(self):
        return f"Kurthi : {self.Brand}\nPrice : ${self.Price}\nSize : {self.size}\nColor : {self.dark_colors}" 

my_product = Color("Chennai silks",57,37,"peach & Lavender")
print(my_product.get_details()) 



# Multiple Inheritance: 
# Parent-1 class:
class MicrowaveAppliance:
    def heat_food(self,minutes):
        return f"Heating food in the microwave for {minutes} minutes"

# Parent-2 class:
class WifiDevice:
    def connect_to_wifi(self):
        return "Connecting to home wifi network"

# Child class:
class smartMicrowave(MicrowaveAppliance,WifiDevice):
    def remote_start(self):
        return "Starting the microwave remotely via smartphone app command."

my_Oven = smartMicrowave()
print(my_Oven.connect_to_wifi())
print(my_Oven.heat_food(2))
print(my_Oven.remote_start()) 



# Hybrid Inheritance:
# Grandparent class:

class Person:
    def __init__(self,Name):
        self.Name = Name
    def get_info(self):
        return f"Person Name:{self.Name}"
# Parent Class:
class Employee(Person):
    def __init__(self,Name,emp_id):
        super().__init__(Name)
        self.emp_id = emp_id
    def clock_in(self):
        return f"{self.Name} has clocked into work.\n{self.Name}:{self.emp_id}"        

# Child class 1:
class Doctor(Employee):
    def __init__(self,Name,emp_id,Specialization):
        super().__init__(Name,emp_id)
        self.Specialization = Specialization
    def prescribed_medicine(self):
        return f"Dr.{self.Name} is specialized in {self.Specialization} writing a Prescription." 
# Child class 2:       
class Nurse(Employee):
    def __init__(self,Name,emp_id,Department):
        super().__init__(Name,emp_id)
        self.Department = Department
    def check_vitals(self):
        return f"Nurse {self.Name} is checking patients heartbeat in the {self.Department}."
#My_Doctor = Doctor("Sureshwar",234156,"Cardiolagist")
#print(My_Doctor.prescribed_medicine())
Nurse = Nurse("Krithi",378560,"General Ward")
print(Nurse.check_vitals()) 