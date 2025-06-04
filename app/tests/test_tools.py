import unittest

from app.tools import *
from ..PersonalAccount import correct_promoCode

class TestTools(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass\n")
        cls.example_promoCode = "PROM_XYZ"
        cls.pesel = "77022556916"
        cls.nip = "6324293512"

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("\ntearDown\n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass!")
    

    
    def test_pesel_checksum(self):
        print("Testing tool pesel_checksum")
        self.assertTrue(pesel_checksum(self.pesel),"pesel_checksum tool unexpected value")
    
    def test_pesel_checkLength(self):
        print("Testing tool pesel_checkLength")
        self.assertFalse(pesel_checkLength(self.pesel),"pesel_checkLength tool unexpected value")
    
    def test_nip_checksum(self):
        print("Testing tool nip_checksum")
        self.assertTrue(nip_checksum(self.nip),"nip_checksum tool unexpected value")
    
    def test_nip_checkLength(self):
        print("Testing tool nip_checkLength")
        self.assertFalse(nip_checkLength(self.nip),"nip_checkLength tool unexpected value")
    
    def test_promo_code_check(self):
        print("Testing tool promo_code_check")
        self.assertFalse(promo_code_check(self.example_promoCode,correct_promoCode),"promo_code_check tool incorrect promo code unexpected value")
        self.assertTrue(promo_code_check(correct_promoCode,correct_promoCode),"promo_code_check tool correct promo code unexpected value")
        self.assertFalse(promo_code_check(None,correct_promoCode),"promo_code_check tool None promo code unexpected value")

    def test_yob_check(self):
        print("Testing tool yob_check")
        self.assertTrue(yob_check("64281577985"),"yob_check for year 2064 unexpected value")
        self.assertTrue(yob_check("71081532461"),"yob_check for year 1971 unexpected value")
        self.assertFalse(yob_check("57081556793"),"yob_check for year 1957 unexpected value")

    def test_last_3_incoming_transactions_check(self):
        print("Testing tool for checking if last 3 transactions were incoming")
        self.assertTrue(last_3_incoming_check([10,12,11]),"last_3_incoming_check unexpected value")
        self.assertFalse(last_3_incoming_check([-1,10,11]),"last_3_incoming_check unexpected value")
        self.assertFalse(last_3_incoming_check([1,0,11]),"last_3_incoming_check unexpected value")

    def test_last_5_transaction_sum_check(self):
        print("Testing tool for summing last 5 transactions")
        self.assertEqual(last_5_transaction_sum([10,12,11,13,14]),60,"last_5_transaction_sum unexpected value")
        self.assertEqual(last_5_transaction_sum([-1,10,-11,-12,3]),-11,"last_5_transaction_sum unexpected value")
        self.assertEqual(last_5_transaction_sum([1,0,11]),0,"last_5_transaction_sum unexpected value")
        self.assertEqual(last_5_transaction_sum([1,2,3,4,5,6,7,8,9,10]),40,"last_5_transaction_sum unexpected value")

    def test_company_Account_Loan_Condition(self):
        print("Testing tool that accepts loan conditions for company account")
        self.assertTrue(company_Account_Loan_Condition(2700,[-1000,1273,1775],1300))
        self.assertFalse(company_Account_Loan_Condition(1500,[1775,1775],750))
        self.assertFalse(company_Account_Loan_Condition(1500,[1,72,3,4,5,6,27,],270))
        self.assertFalse(company_Account_Loan_Condition(1500,[],1500))
        self.assertFalse(company_Account_Loan_Condition(2700,[-1000,1273,1775],0))
        self.assertTrue(company_Account_Loan_Condition(650,[1775,1775,1775,1775,1775,1775],127))
