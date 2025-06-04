import unittest

from unittest.mock import MagicMock

from datetime import date

from ..SMTPClient import SMTPClient

from ..PersonalAccount import PersonalAccount
from ..CompanyAccount import CompanyAccount


class TestSendHistoryToEmail(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_personal_account = PersonalAccount("Bob","Example","97111883785")
        cls.test_personal_account.incoming_transfer(100)
        cls.test_company_account = CompanyAccount("CompanyName","4661938857")
        cls.test_company_account.incoming_transfer(1000)
        cls.correctSubject = f"Wyciąg z dnia {date.today()}"
        cls.correctCompanyAccountText = "Historia konta Twojej firmy to: [1000.0]"
        cls.correctPersonalAccountText = "Twoja historia konta to: [100.0]"
        print("setUpClass!\n")

    def setUp(self):
        print("setUp\n")

    def tearDown(self):
        print("tearDown\n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass!\n")


    def test_send_history_personal_account_true(self):
        SMTPClient.send = MagicMock(return_value=True)
        result = self.test_personal_account.send_history_to_email("example@gmail.com")
        self.assertTrue(result)
        SMTPClient.send.assert_called_once_with(self.correctSubject, self.correctPersonalAccountText,"example@gmail.com")

    def test_send_history_company_account_true(self):
        SMTPClient.send = MagicMock(return_value=True)
        result = self.test_company_account.send_history_to_email("example@gmail.com")
        self.assertTrue(result)
        SMTPClient.send.assert_called_once_with(self.correctSubject, self.correctCompanyAccountText,"example@gmail.com")

    def test_send_history_personal_account_false(self):
        SMTPClient.send = MagicMock(return_value=False)
        result = self.test_personal_account.send_history_to_email("example@gmail.com")
        self.assertFalse(result)
        SMTPClient.send.assert_called_once_with(self.correctSubject, self.correctPersonalAccountText,"example@gmail.com")

    def test_send_history_company_account_false(self):
        SMTPClient.send = MagicMock(return_value=False)
        result = self.test_company_account.send_history_to_email("example@gmail.com")
        self.assertFalse(result)
        SMTPClient.send.assert_called_once_with(self.correctSubject, self.correctCompanyAccountText,"example@gmail.com")
