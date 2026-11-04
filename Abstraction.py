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



