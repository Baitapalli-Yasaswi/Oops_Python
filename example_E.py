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