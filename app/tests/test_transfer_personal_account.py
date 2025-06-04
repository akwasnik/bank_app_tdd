import unittest
from ..PersonalAccount import PersonalAccount

class TestTransferAccountingForPersonalAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass\n")
        name = "Bob"
        surname = "Example"
        pesel = "97111883785"
        cls.test_personal_account = PersonalAccount(name,surname,pesel)

    def setUp(self):
        print("setUp")

    def tearDown(self):
        self.test_personal_account.balance = 0
        print("\ntearDown\n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass!")



    def test_incoming_transfer(self):
        print("Testing incoming transfer (PERSONAL ACCOUNT)")
        self.test_personal_account.incoming_transfer(100)
        self.assertEqual(self.test_personal_account.balance,100,"Incorrect incoming transfer!")

    def test_outgoing_transfer(self):
        print("Testing outgoing transfer (PERSONAL ACCOUNT)")
        self.test_personal_account.balance = 100
        self.test_personal_account.outgoing_transfer(100)
        self.assertEqual(self.test_personal_account.balance,0, "Incorrect outgoing transfer!")
    
    def test_outgoing_transfer_insufficient_funds(self):
        print("Testing outgoing transfer with insufficient funds (PERSONAL ACCOUNT)")
        self.test_personal_account.balance = 80
        self.test_personal_account.outgoing_transfer(100)
        self.assertEqual(self.test_personal_account.balance,80, "Incorrect outgoing transfer with insufficient funds !")
    
    def test_series_of_transfers(self):
        print("Testing series of transfers (PERSONAL ACCOUNT)")
        self.test_personal_account.incoming_transfer(1000)
        self.test_personal_account.outgoing_transfer(250)
        self.test_personal_account.incoming_transfer(10.25)
        self.assertEqual(self.test_personal_account.balance,760.25," Incorrect series of transfers !")

    def test_outgoing_express_transfer(self):
        print("Testing outgoing express transfer (PERSONAL ACCOUNT)")
        self.test_personal_account.balance = 100
        self.test_personal_account.outgoing_express_transfer(80)
        self.assertEqual(self.test_personal_account.balance,19,"Incorrect outgoing express transfer !")

    def test_outgoing_express_transfer_debt_possibility(self):
        print("Testing outgoing express transfer debt possibility (PERSONAL ACCOUNT)")
        self.test_personal_account.balance = 80
        self.test_personal_account.outgoing_express_transfer(80)
        self.assertEqual(self.test_personal_account.balance,-1,"Incorrect outgoing express transfer with debt !")

    def test_outgoing_express_transfer_insufficient_funds(self):
        print("Testing outgoing express transfer insufficient funds (Personal ACCOUNT)")
        self.test_personal_account.balance = 40
        self.assertFalse(self.test_personal_account.outgoing_express_transfer(80))