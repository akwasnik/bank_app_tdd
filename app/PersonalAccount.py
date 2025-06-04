from .Account import Account

correct_promoCode = "PROM_G32"

from app.tools import *

class PersonalAccount(Account):
    def __init__(self, name: str, surname: str, pesel, promoCode=None):
        super().__init__()
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.pesel = pesel
        self.promoCode = promoCode

        if pesel_checkLength(self.pesel):
            self.pesel = "Incorrect pesel!"

        if promo_code_check(self.promoCode,correct_promoCode) and yob_check(self.pesel):
            self.balance += 50

        if not(self.name.isalpha()):
            self.name = "Incorrect name!"
            
        if not(self.surname.isalpha()):
            self.surname = "Incorrect surname!"

    def loan(self, amount:int ):
        if last_3_incoming_check(self.history) or last_5_transaction_sum(self.history) > amount:
            self.balance+=amount