from .SMTPClient import SMTPClient
from datetime import date

class Account:
    def __init__(self):
        self.balance = 0
        self.history = []

    def incoming_transfer(self,amount):
        self.balance+=float(amount)
        self.history.append(float(amount))

    def outgoing_transfer(self,amount):
        if self.balance >= float(amount):
            self.balance -= float(amount)
            self.history.append(-float(amount))
            return True
        else:
            return False
            
    def outgoing_express_transfer(self,amount):
        className = self.__class__.__name__
        additional_payment = 1 if className == "PersonalAccount" else 5
        if self.balance >= float(amount):
            self.balance -= additional_payment+float(amount)
            self.history.append(-float(amount))
            self.history.append(-additional_payment)
            return True
        else:
            return False

    def send_history_to_email(self,email_address):
        className = self.__class__.__name__
        subject = f"Wyciąg z dnia {date.today()}"
        text = f"Twoja historia konta to: {self.history}" if className == "PersonalAccount" else f"Historia konta Twojej firmy to: {self.history}"
        return SMTPClient.send(subject,text,email_address)