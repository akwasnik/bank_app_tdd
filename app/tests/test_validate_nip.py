import unittest

from unittest.mock import Mock,patch

from ..CompanyAccount import CompanyAccount


class TestValidateNip(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.correct_nip="8461627563"
        cls.incorrect_nip="8461627593"
        cls.too_long_nip="8461627593111"
        print("setUpClass\n")

    def setUp(self) -> None:
        print("setUp\n")

    def tearDown(self) -> None:
        print("tearDown\n")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass!")

    @patch("requests.get")
    def test_validate_correct_nip(self,mock_get):
        print("Running test: Validate with correct nip")

        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        test_company_account=CompanyAccount("random",self.correct_nip)
        self.assertTrue(test_company_account.validate_nip(self.correct_nip))
    
    @patch("requests.get")
    def test_validate_other_status_code(self,mock_get):
        print("Running test: Validate with other status code")

        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        test_company_account=CompanyAccount("random",self.correct_nip)
        self.assertFalse(test_company_account.validate_nip(self.correct_nip))


    @patch("requests.get")
    def test_validate_incorrect_nip(self,mock_get):
        print("Running test: Validate with incorrect nip")

        mock_response = Mock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response

        with self.assertRaises(ValueError):
            CompanyAccount("Test Company", self.incorrect_nip)
