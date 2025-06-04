import unittest

from ..PersonalAccount import PersonalAccount
from ..CompanyAccount import CompanyAccount
from ..AccountRegistry import AccountRegistry


class testAccountRegistry(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass!\n")
        cls.test_personal_account_1 = PersonalAccount("Bob","Example","61110213876")
        cls.test_personal_account_2 = PersonalAccount("John","Doe","80010645279")

    def setUp(self):
        AccountRegistry.registry = []
        print("setUp")

    def tearDown(self):
        print("\ntearDown\n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass!")



    def test_add_account(self):
        print("Running test: adding an account to AccountRegistry")
        AccountRegistry.add_account(self.test_personal_account_1)
        self.assertEqual(AccountRegistry.registry[0],self.test_personal_account_1)

    def test_count_accounts(self):
        print("Running test: counting accounts")
        AccountRegistry.add_account(self.test_personal_account_1)
        AccountRegistry.add_account(self.test_personal_account_2)
        self.assertEqual(AccountRegistry.get_accounts_count(),2)

    def test_search_empty_registry(self):
        print("Running test: searching with empty registsry")
        AccountRegistry.add_account(self.test_personal_account_1)
        AccountRegistry.add_account(self.test_personal_account_2)
        self.assertIsNone(AccountRegistry.search_by_pesel("123"))

    
    def test_search_not_existing_pesel(self):
        print("Running test: searching with empty registsry")
        self.assertIsNone(AccountRegistry.search_by_pesel("123"))


    def test_search_by_pesel(self):
        print("Running test: searching account by pesel")
        AccountRegistry.add_account(self.test_personal_account_1)
        AccountRegistry.add_account(self.test_personal_account_2)
        search_result = AccountRegistry.search_by_pesel(self.test_personal_account_1.pesel)
        self.assertEqual(search_result,self.test_personal_account_1)
    