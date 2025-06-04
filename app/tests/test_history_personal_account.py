import unittest

from ..PersonalAccount import PersonalAccount

#

class TestAccountHistoryPersonalAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass\n")
        cls.test_personal_account = PersonalAccount("Bob","Example","97111883785")
        
    def setUp(self):
        self.test_personal_account.balance = 100
        self.test_personal_account.history=[]
        print("setUp")

    def tearDown(self):
        print("\ntearDown\n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass!")


    
    def test_history_incoming_transfer(self):
        print("Testing history for incoming transfer")
        self.test_personal_account.incoming_transfer(100)
        self.assertEqual(self.test_personal_account.history,[100],"first example")
    
    def test_history_outgoing_transfer(self):
        print("Testing history for outgoing transfer")
        self.test_personal_account.outgoing_transfer(100)
        self.assertEqual(self.test_personal_account.history,[-100],"second example")
    
    def test_history_outgoing_transfer_insufficient_funds(self):
        print("Testing history for outgoing transfer with insufficient funds")
        self.test_personal_account.outgoing_transfer(120)
        self.assertEqual(self.test_personal_account.history,[],"third example")

    def test_history_outgoing_express_transfer(self):
        print("Testing history for outgoing express transfer")
        self.test_personal_account.outgoing_express_transfer(100)
        self.assertEqual(self.test_personal_account.history,[-100,-1],"fourth example")

    def test_history_series_of_transfers(self):
        print("Testing history for series of transfers")
        self.test_personal_account.incoming_transfer(120)
        self.test_personal_account.outgoing_transfer(50)
        self.test_personal_account.outgoing_express_transfer(30)
        self.assertEqual(self.test_personal_account.history,[120,-50,-30,-1],"fifth example")