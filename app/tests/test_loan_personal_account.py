import unittest

from ..PersonalAccount import PersonalAccount

from parameterized import parameterized

class TestLoanPersonalAccount(unittest.TestCase):

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
        self.test_personal_account.history=[]
        self.test_personal_account.balance=0
        print("\ntearDown\n")


    @classmethod
    def tearDownClass(cls):
        print("tearDownClass!")



    @parameterized.expand([
        ("test loan 3 incoming", [30, 30, 30], 90, 90),
        ("test loan last 5 higher", [30, -30, -30, 30, 30], 20, 20),
        ("test loan last 5 lower", [30, -30, -30, 30, -30], 20, 0),
        ("test loan no history", [], 100, 0),
        ("test loan too short history", [10, -10], 5, 0),
    ])

    def test_parameterized_loan_PersonalAccount(self, name, history, loan_amount, expected):
        print(f"Running test: {name}")
        self.test_personal_account.history = history
        self.test_personal_account.loan(loan_amount)
        self.assertEqual(self.test_personal_account.balance, expected, "Incorrect expected balance!")