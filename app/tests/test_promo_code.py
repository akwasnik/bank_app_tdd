import unittest

from ..PersonalAccount import PersonalAccount,correct_promoCode
from app.tools import yob_check

class TestPromoCodeCorrectCode(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass\n")
        cls.test_account_correct_promoCode = PersonalAccount("Bob","Example","97111883785",correct_promoCode)
        cls.test_account_no_promoCode = PersonalAccount("Mathew","Harbor","97111883785")
        # "54122072559" example pesel for incorrect yob_check

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("\ntearDown\n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass!")



    def test_promoCode_is_none(self):
        print("No promo code test")
        self.assertIsNone(self.test_account_no_promoCode.promoCode,"No promo code expected None value!")

    def test_balance_no_promoCode(self):
        print("No promo code account balance test")
        self.assertEqual(self.test_account_no_promoCode.balance, 0, "Balance is not 0 for no promo code account!") 

    def test_correct_promoCode(self):
        print("Feature 4 test")
        self.assertEqual(len(self.test_account_correct_promoCode.promoCode),8, "Incorrect promo code length!")
        self.assertEqual(self.test_account_correct_promoCode.promoCode,correct_promoCode, "Incorrect promo code!")
        self.assertEqual(self.test_account_correct_promoCode.balance,50,"Promo code was not applied!")

    def test_correct_yob(self):
        print("Feature 5 test")
        self.assertTrue(yob_check(self.test_account_correct_promoCode.pesel),"Yob leq to 1960!")

