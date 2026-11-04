"""
class student:
    def __init__(self,name,age,grno):
        self.__name = name
        self.__age = age 
        self.__grno = grno   

    
    def get_name(self):
        return self.__name 
    def get_age(self):
        return self.__age
    def get_grno(self):
        return self.__grno
       

student("Rahul",23,125640)
#print(student.get_name())        
#print(student.get_age())
#print(student.get_grno()) 
"""

"""
class Dog:
    def __init__(self,name):
        self.name = name
        


    def bark(self):
        print(f"{self.name} says bowww!")

dog1 = Dog("Buddy")
dog2 = Dog("Max")  

dog1.bark() 
dog2.bark()  
""" 

"""
class Dog:
    def __init__(self,name,age):
        self.__name = name # "__" are use to keep the information private.
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age

dog1 = Dog("Max",12)
print(dog1.get_name())
print(dog1.get_age()) 
"""  
"""
class Hostel_girls_info:
    def __init__(self,name,roomno):
        self.__name = name
        self.__roomno = roomno
    def get_name(self):
        return self.__name
    def get_roomno(self):
        return self.__roomno
   

Girl_1 = Hostel_girls_info("Lashya",405)
print(Girl_1.get_name())
Girl_2 = Hostel_girls_info("Vachana",404)
print(Girl_2.get_name())
print(Girl_2.get_roomno()) 
""" 
"""
class A:
    def __init__(self,M1,M2):
        self.M1 = M1
        self.M2 = M2
    def get_details(self):
        return f"This is method {self.M1}\nThis is method {self.M2}"    

class B(A):
    def __init__(self,M3):
        super().__init__("M1", "M2")  # Call the parent class constructor
        self.M3 = M3
    def get_datails2(self):
        return f"This is the method {self.M1}\nThis is the method {self.M2}\nThis is the method {self.M3}"

my_method = A("M1","M2")
#print(my_method.get_details())    
my_method2 = B("M3")
print(my_method2.get_datails2()) 
""" 
"""
class A:
    def __init__(self,a,b,c,d,e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
    def Addition(self):
        return "Addition of two numbers is: " + str(self.a + self.b)
add = A(10,20,30,40,50)    
print(add.Addition())
class B:
    def __init__(self,f,g,h):
        self.f = f
        self.g = g
        self.h = h
    def Add (self):
        return "Addition of three numbers is:" + str(self.f +self.g + self.h)
add2 = B(80,60,70)
print(add2.Add())
# without accessing the parent class A 
""" 

class Animal:
    def __init__(self,Eating,Sleeping):
        self.Eating = Eating
        self.Sleeping = Sleeping
    def get_details(self):
        return f"Animal is {self.Eating} and {self.Sleeping}"
class Dog():     
    def __init__(self,Name,Age,Speciality):
        self.Name = Name
        self.Age = Age
        self.Speciality = Speciality
    def Speciality(self):
        return f"{self.Name} {self.Speciality} at night!,everyday!"
dog = Dog("Buddy",12,"Barks") 
print(dog.get_details())  
print(dog.Speciality())          












from abc import ABC, abstractmethod 

class Restaurant(ABC):

    def __init__(self,name):
        self.name = name

    @abstractmethod
    def prepare_food(self):
        pass

    def print_bill(self,item,price):
        return f"Bill for {item} is ${price}."

class ItalianRestaurant(Restaurant):
    def prepare_food(self,name,item):
        return f"Preparing delicious {item} at {name}."
class AmericanRestaurant(Restaurant):
    def prepare_food(self,name,item):
        return f"Preparing tasty {item} at {name}."

Restaurant1 = ItalianRestaurant("Gastronomia")
print(Restaurant1.prepare_food(Restaurant1.name,"pasta"))
Restaurant2 = AmericanRestaurant("Burger King")
print(Restaurant2.prepare_food(Restaurant2.name,"Burger"))      
 

from abc import ABC, abstractmethod 
class Vehicle(ABC):
    def __init__(self,Brand,Model):
        self.Brand=Brand
        self.Model=Model
    @abstractmethod
    def perform_service(self):
        pass

class Car(Vehicle):
    def perform_service(self):
        return f"Performance service for {self.Brand} {self.Model} is completed"

class Bike(Vehicle):
    def perform_service(self):
        #pass 
        return f"Performance service for {self.Brand} {self.Model} is completed"        
vehicle1 = Bike("Honda", "CBR")
print(vehicle1.perform_service())
print("Did it reach here?") 
vehicle2 = Car("Toyota", "Camry")
print(vehicle2.perform_service())    


# Notification System:
from abc import ABC, abstractmethod
class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self,message):
        pass

class EmailNotification(NotificationSender):
    def send_notification(self,user,message):
        return f"Sending email to {user}: {message}"

class WhatsAppNotification(NotificationSender):
    def send_notification(self,user,message):
        return f"Sending WhatsApp message to {user}: {message}"

Remainder1 = EmailNotification()        
print(Remainder1.send_notification("Raghu", "Your order has been shipped."))
Remainder2 = WhatsAppNotification()
print(Remainder2.send_notification("Sreekar", "Your appointment is confirmed."))