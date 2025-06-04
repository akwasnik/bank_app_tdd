import unittest

from ..CompanyAccount import CompanyAccount

from parameterized import parameterized

class TestLoanCompanyAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass\n")
        company_name = "BobMasters"
        nip = "4661938857"
        cls.test_company_account = CompanyAccount(company_name,nip)
        

    def setUp(self):
        print("setUp")
        

    def tearDown(self):
        self.test_company_account.history=[]
        print("\ntearDown\n")


    @classmethod
    def tearDownClass(cls):
        print("tearDownClass!")



    @parameterized.expand([
        ("test loan correct balance and ZUS paid", [1775], 100, 1875),
        ("test loan incorrect balance and ZUS paid", [1775,1000], 2700, 2775),
        ("test loan correct balance and ZUS not paid", [100,100,100,-100,-100], 49, 100),
        ("test loan incorrect balance and ZUS not paid", [100,100,100,-100,-100], 100, 100),
        ("test loan correct balance and ZUS paid", [27,1775,1,3,4], 200, 2010),
    ])

    def test_parameterized_loan_CompanyAccount(self, name, history, loan_amount, expected):
        print(f"Running test: {name}")
        self.test_company_account.history = history
        self.test_company_account.balance = sum(history)
        self.test_company_account.loan(loan_amount)
        self.assertEqual(self.test_company_account.balance, expected, "Incorrect expected balance!")
