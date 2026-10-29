class Netflix:
    def play_media(self,Name):
        return f"Streaming Hd movie:{Name} from Netflix."
class Spotify:
    def play_media(self,Name):
        return f"Playing audio track:{Name} from spotify."
class Youtube:
    def play_media(self,Name):
        return f"Playing Oops tutorial in {Name} on youtube." 
def remote_control_button(media_device,Name):
    print(media_device.play_media(Name))
netflix = Netflix()
spotify = Spotify()
youtube = Youtube()
remote_control_button(netflix,"Paradise")
remote_control_button(spotify,"Raja")
remote_control_button(youtube,"Code_with_Harry")    


class Netflix:
    def __init__(self,Name):
        self.Name = Name
    def play_media(self):
        return f"Streaming Hd movie:{self.Name} from Netflix."
class Spotify:
    def __init__(self,Name):
        self.Name = Name
    def play_media(self):
        return f"Playing audio track: {self.Name} from spotify."
class Youtube:
    def __init__(self,Name):
        self.Name = Name
    def play_media(self):
        return f"Playing {self.Name} channel tutorial on youtube."
def remote_control_button(media_device):
    print(media_device.play_media())
netflix = Netflix("Paradise")
spotify = Spotify("Phil shur")
youtube = Youtube("Oops")
remote_control_button(netflix)
remote_control_button(spotify)
remote_control_button(youtube)



class CreditCardpayment:
    def process_payment(self,amount):
        #self.amount = amount
        return f"Processing {amount} payment through credit card."
class Paypalpayment:
    def process_payment(self,amount):
        #self.amount = amount
        return f"Processing {amount} through paypal."
class Googlepaypayment:
    def process_payment(self,amount):
        #self.amount = amount
        return f"Processing Rs.{amount} through google pay."
def checkout(payment_gateway, amount):
    print(payment_gateway.process_payment(amount))
CCP = CreditCardpayment()
PPP = Paypalpayment()
GPP = Googlepaypayment()
checkout(CCP,1000)
checkout(PPP,700)
checkout(GPP, 300)




# EXAMPLE "NOT TO DO" Method Overloading:

class MathOperations:
    def add(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        return f"Addition of three numbers are :{self.a+self.b+self.c}"
    def sub(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        return f"Subtraction of three numbers are :{self.a-self.b-self.c}"   
    def mul(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        return f"Multiplication of three numbers are :{self.a*self.b*self.c}" 
math = MathOperations()
print(math.add(10,20,30))
print(math.sub(30,10,10))
print(math.mul(10,20,30))


# Method Overloading:

class MathOperations:
    def add(self,a,b,c):
        return f"Addition of three numbers are :{a+b+c}"
math = MathOperations()
print(math.add(10,20,30))    




# Method Overriding:
class Payment:
    def Process_Payment(self,Amount):
        return f"pay the amount {Amount} through the given Options"
class Creditcardpayment(Payment):    
    def Process_Payment(self,Amount):
        return  f"Pay your amount {Amount} through credit card"
class Googlepayment(Payment):
    def Process_Payment(self,Amount):
        return f"Pay your amount {Amount} through Google pay"   
payments = [Creditcardpayment(), Googlepayment()]
for p in payments:
    print(p.Process_Payment(1000))



payment_method_1 = Creditcardpayment()
print(payment_method_1.Process_Payment(1000)) 
payment_method_2 = Googlepayment()   
print(payment_method_2.Process_Payment(3500))



class Notifications:
    def send_Notifications(self,Message):
        return "Sending Notifications."
class WhatsApp(Notifications):
    def send_Notifications(self,Message):   
        return f"I got my \'{Message}\' notification through flipkart"
class Email(Notifications):
    def send_Notifications(self,Message):
        return f"I got the notification \'{Message}\' from the WXT company!"
Notification1 = WhatsApp()
print(Notification1.send_Notifications("Your order delivered successfully!"))
Notification2 = Email()
print(Notification2.send_Notifications("We are Hiring you as a Project_Manager in WXT company\nCongratulation!"))         


# Method Overloading: 
class SmartLight:
    def action(self,Press):
        if Press == 1:
            print("If we press it once the light will glow normal brightness")
        elif Press == 2:
            print("If we press twice the light wiill glow with different colors")
        else :
            print("If we hold it for few seconds then the light brightness gets dim ")
Light = SmartLight()
Light.action(1)
Light.action(2)
Light.action(0)


                       
