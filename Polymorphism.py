
class Netflix:
    def play_media(self):
        return "Streaming Hd movie: Stranger things from Netflix."
class Spotify:
    def play_media(self):
        return "Playing audio track: Lo-Fi beats from spotify."
class Youtube:
    def play_media(self):
        return "Playing Oops tutorial on youtube." 
def remote_control_button(media_device):
    print(media_device.play_media())
netflix = Netflix()
spotify = Spotify()
youtube = Youtube()
remote_control_button(netflix)
remote_control_button(spotify)
remote_control_button(youtube)    

"""
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
""" 


class CreditCardpayment:
    def process_payment(self,amount):
        self.amount = amount
        return f"Processing {self.amount} payment through credit card."
class Paypalpayment:
    def process_payment(self,amount):
        self.amount = amount
        return f"Processing {self.amount} through paypal."
class Googlepaypayment:
    def process_payment(self,amount):
        self.amount = amount
        return f"Processing Rs.{self.amount} through google pay."
def checkout(payment_gateway, amount):
    print(payment_gateway.process_payment(amount))
CCP = CreditCardpayment()
PPP = Paypalpayment()
GPP = Googlepaypayment()
checkout(CCP,1000)
checkout(PPP,700)
checkout(GPP, 300)