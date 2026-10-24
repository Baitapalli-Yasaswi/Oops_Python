"""
class Rectangle:
    def area(self,length,width):
        self.__length = length
        self.__width = width
    def get_length(self):
        return self.length
    def get_width(self):
        return self.width 
    def area(self,l,w):
        if l > 0 and w > 0:
            area = l*w
            print(f"Area of the Rectangle:{area}")
        else:
            print("It is invalid")    
""" 
# Hybrid Inheritance.
# Hierarchical Inheritance + Multiple Inheritance:
# Parent class: 
class Appliance:
    def __int__(self,Brand):
        self.Brand = Brand
    def plug_in(self):
        return f"{self.Brand} connected to power outlet."
# Child class-1: / Branch-1
class Oven(Appliance):
    def __init__(self,Brand,Price):
        super().__init__(Brand)
        self.Price = Price 
    def get_details(self):
        return f"{self.Brand} Oven Bakes the food perfectly & it is very tasty to eat.\n{self.Brand}:{self.Price} "   
# Child class-2: / Branch-2     
class Fridge(Appliance):
    def __init__(self,Brand,Price,Watt_capacity):
        super().__init__(Brand)
        self.Price = Price
        self.Watt_capacity = Watt_capacity
    def working_condition(self):
        return f"{self.Brand} fridge has {self.Watt_capacity}\n{self.Brand}fridge:{self.Price}"            
# child Class(combing of Branch-1 & Branch-2) --> It act as Multiple Inheritance:
class New_Restaurant(Oven,Fridge):
    def __init__(self,Brand,Price,Watt_capacity,Place):
        super().__init__(Brand,Price,Watt_capacity)
        self.Place = Place
    def Res_details(self): 
        return f"This Restaurant is at {self.Place}.It is famous for Breadtoast and self_made ice-creams"  
    my_appliance = Oven("Yurel",12000)
    print(my_appliance.get_details()) 