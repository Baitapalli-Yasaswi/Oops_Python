from abc import ABC, abstractmethod
class Payment(ABC):
    
    @abstractmethod
    def process_payment(self,amount):
        pass
    def print_receipt(self):
        return "Printing official transaction receipt...."

class CreditcardPayment(Payment):
    def process_payment(self,amount):
        return f"Processing {amount} payment through credit card."


class Paypalpayment(Payment):
    def process_payment(self,amount):
        return f"Processing {amount} through paypal."


Cc = CreditcardPayment()
print(Cc.print_receipt())
print(Cc.process_payment(10000))

Pp = Paypalpayment()
print(Pp.print_receipt())
print(Pp.process_payment(30000))
 


from abc import ABC, abstractmethod 

class ATM(ABC):

    @abstractmethod
    def insert_card(self):
        pass
    @abstractmethod
    def enter_pin(self):
        pass


    def print_welcome_message(self):
        return "Welcome to National Secure Bank ATM"
class SBI(ATM):
    def insert_card(self):
        return "Card inserted into the machine."
    def enter_pin(self):
        return "Pin entered successfully."
class AXIS(ATM):
    def insert_card(self):
        return "Card inserted into the machine."
    def enter_pin(self):
        return "Pin entered successfully."

Bank1 = SBI()
print(Bank1.print_welcome_message())        
print(Bank1.insert_card())
print(Bank1.enter_pin())

Bank2 = AXIS()
print(Bank2.print_welcome_message())
print(Bank2.insert_card())
print(Bank2.enter_pin())

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



