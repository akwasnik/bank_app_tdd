import unittest

from ..PersonalAccount import PersonalAccount
from app.tools import pesel_checksum

class TestCreateBankAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        name = "Bob"
        surname = "Example"
        pesel = "97111883785"
        cls.test_personal_account = PersonalAccount(name,surname,pesel)
        
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("\ntearDown\n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass!")



    def test_create_account(self):
        print("Feature 1 test")
        self.assertEqual(self.test_personal_account.name, "Bob", "Name was not saved!")
        self.assertEqual(self.test_personal_account.surname, "Example", "Surname was not saved!")
        self.assertEqual(self.test_personal_account.balance, 0, "balance is not 0!") 

    def test_incorrect_pesel(self):
        print("Test incorrect pesel")
        test_personal_account = PersonalAccount("Bob","Example", "123")
        self.assertEqual(test_personal_account.pesel,"Incorrect pesel!")

    def test_name_and_surname_isAlpha(self):
        print("Name and surname isalpha test")
        test_personal_account = PersonalAccount("R2D2","C3PO","97111883785")
        self.assertEqual(test_personal_account.name,"Incorrect name!","Name must contain only letters!")
        self.assertEqual(test_personal_account.surname,"Incorrect surname!","Surname must contain only letters!")
    
    def test_create_pesel(self):
        print("Feature 2 test")
        self.assertEqual(self.test_personal_account.pesel,"97111883785","Pesel was not saved !")

    def test_correct_pesel(self):
        print("Feature 3 test")
        self.assertEqual(len(self.test_personal_account.pesel),11,"Pesel must have 11 digits !") # feature_3 test
        self.assertEqual(len(list(filter(lambda x: x.isdigit(),self.test_personal_account.pesel))),11,"Pesel must contain only digits !") # additional test
        self.assertTrue(pesel_checksum(self.test_personal_account.pesel),"Wrong checksum for pesel !") # additional test
