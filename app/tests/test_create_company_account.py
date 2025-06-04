import unittest

from ..CompanyAccount import CompanyAccount
from app.tools import nip_checksum

class TestCreateBankAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass\n")
        company_name = "BobMasters"
        nip = "4661938857"
        cls.test_company_account = CompanyAccount(company_name,nip)
        
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("\ntearDown\n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass!")



    def test_create_account(self):
        print("Feature 1 test")
        self.assertEqual(self.test_company_account.company_name, "BobMasters", "Company name was not saved!")

    def test_incorrect_nip(self):
        print("Test incorrect nip")
        test_dummy = CompanyAccount("BobMasters", "123")
        self.assertEqual(test_dummy.nip,"Incorrect nip!")

    def test_create_nip(self):
        print("Feature 2 test")
        self.assertEqual(self.test_company_account.nip,"4661938857","Nip was not saved !")

    def test_correct_nip(self):
        print("Feature 3 test")
        self.assertEqual(len(self.test_company_account.nip),10,"Nip must have 10 digits !")
        self.assertEqual(len(list(filter(lambda x: x.isdigit(),self.test_company_account.nip))),10,"Nip must contain only digits !") 
        self.assertTrue(nip_checksum(self.test_company_account.nip),"Wrong checksum for nip !")