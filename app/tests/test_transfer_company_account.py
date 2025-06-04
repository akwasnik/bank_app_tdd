import unittest
from ..CompanyAccount import CompanyAccount

class TestTransferAccountingForCompanyAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass\n")
        company_name = "BobMasters"
        nip = "4661938857"
        cls.test_company_account = CompanyAccount(company_name,nip)

    def setUp(self):
        print("setUp")

    def tearDown(self):
        self.test_company_account.balance = 0
        print("\ntearDown\n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass!")



    def test_incoming_transfer(self):
        print("Testing incoming transfer (COMPANY ACCOUNT)")
        self.test_company_account.incoming_transfer(100)
        self.assertEqual(self.test_company_account.balance,100,"Incorrect incoming transfer!")

    def test_outgoing_transfer(self):
        print("Testing outgoing transfer (COMPANY ACCOUNT)")
        self.test_company_account.balance = 100
        self.test_company_account.outgoing_transfer(100)
        self.assertEqual(self.test_company_account.balance,0, "Incorrect outgoing transfer!")
    
    def test_outgoing_transfer_insufficient_funds(self):
        print("Testing outgoing transfer with insufficient funds (COMPANY ACCOUNT)")
        self.test_company_account.balance = 80
        self.test_company_account.outgoing_transfer(100)
        self.assertEqual(self.test_company_account.balance,80, "Incorrect outgoing transfer with insufficient funds !")
    
    def test_series_of_transfers(self):
        print("Testing series of transfer (COMPANY ACCOUNT)")
        self.test_company_account.incoming_transfer(1000)
        self.test_company_account.outgoing_transfer(250)
        self.test_company_account.incoming_transfer(10.25)
        self.assertEqual(self.test_company_account.balance,760.25," Incorrect series of transfers !")

    def test_outgoing_express_transfer(self):
        print("Testing outgoing express transfer (COMPANY ACCOUNT)")
        self.test_company_account.balance = 100
        self.test_company_account.outgoing_express_transfer(80)
        self.assertEqual(self.test_company_account.balance,15,"Incorrect outgoing express transfer !")

    def test_outgoing_express_transfer_debt_possibility(self):
        print("Testing outgoing express transfer debt possibility (COMPANY ACCOUNT)")
        self.test_company_account.balance = 80
        self.test_company_account.outgoing_express_transfer(80)
        self.assertEqual(self.test_company_account.balance,-5,"Incorrect outgoing express transfer with debt !")

    def test_outgoing_express_transfer_insufficient_funds(self):
        print("Testing outgoing express transfer insufficient funds (COMPANY ACCOUNT)")
        self.test_company_account.balance = 40
        self.assertFalse(self.test_company_account.outgoing_express_transfer(80))