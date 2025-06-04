from .Account import Account

import os

os.system('export BANK_APP_MF_URL="https://wl-test.mf.gov.pl/"')
validateUrl = os.getenv('BANK_APP_MF_URL',"https://wl-test.mf.gov.pl/")

import requests,datetime

from app.tools import nip_checkLength,company_Account_Loan_Condition

class CompanyAccount(Account):
    def __init__(self, company_name, nip):
        super().__init__()
        self.company_name = company_name
        self.nip = nip
        if nip_checkLength(self.nip):
            self.nip = "Incorrect nip!"
        else:
            self.validate_nip(nip)

    def loan(self, amount:int ):
        if company_Account_Loan_Condition(self.balance,self.history,amount):
            self.balance+=amount

    def validate_nip(self,nip):
        url = f"{validateUrl}/api/search/nip/{nip}?date={datetime.date.today()}"
        response = requests.get(url)
        if (response.status_code == 200):
            print(response.json())
            return True
        elif (response.status_code == 400):
            raise ValueError("Company not registered!!")
        else:
            return False