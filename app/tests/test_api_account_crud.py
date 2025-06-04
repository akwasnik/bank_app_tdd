import requests
import unittest

from unittest.mock import patch, MagicMock

class TestAccountCrud(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass\n")
        cls.url = "http://127.0.0.1:5000/api/accounts"
        cls.payload = {
            "name": "Bob",
            "surname": "Example",
            "pesel": "97111883785"
        }

    @patch("requests.post")
    def setUp(self, mock_post) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"message": "Account created"}
        mock_post.return_value = mock_response
        
        self.c_response = requests.post(self.url, json=self.payload)
        print("setUp\n")

    @patch("requests.delete")
    def tearDown(self, mock_delete) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Account deleted"}
        mock_delete.return_value = mock_response

        self.d_response = requests.delete(f"{self.url}/{self.payload['pesel']}")
        print("tearDown\n")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass!")

    @patch("requests.post")
    def test_create_account(self, mock_post):
        print("Running test: Account Creation (API)")
        
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"message": "Account created"}
        mock_post.return_value = mock_response
        
        response = requests.post(self.url, json=self.payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["message"], "Account created")

    
    @patch("requests.post")
    def test_create_account_already_existing_pesel(self, mock_post):
        print("Running test: Already existing pesel (API)")
        
        mock_response = MagicMock()
        mock_response.status_code = 409
        mock_response.json.return_value = {"message": "Pesel is in use"}
        mock_post.return_value = mock_response

        response = requests.post(self.url, json={"name": "Bob2", "surname": "Example2", "pesel": self.payload["pesel"]})
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json()["message"], f"Pesel is in use")


    @patch("requests.get")
    def test_get_account_count(self, mock_get):
        print("Running test: Account Count GET method (API)")

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"AccountCount": 1}
        mock_get.return_value = mock_response

        response = requests.get(f"{self.url}/count")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["AccountCount"], 1)

    @patch("requests.get")
    def test_get_account_by_pesel(self, mock_get):
        print("Running test: Get account by pesel (API)")

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = requests.get(f"{self.url}/{self.payload['pesel']}")
        self.assertEqual(response.status_code, 200)
    
    @patch("requests.patch")
    @patch("requests.get")
    def test_update_account(self, mock_get, mock_patch):
        print("Running test: Account Update (API)")

        mock_patch_response = MagicMock()
        mock_patch_response.status_code = 200
        mock_patch_response.json.return_value = {"message": "Account updated"}
        mock_patch.return_value = mock_patch_response

        mock_get_response = MagicMock()
        mock_get_response.status_code = 200
        mock_get_response.json.return_value = {"name": "John"}
        mock_get.return_value = mock_get_response

        u_response = requests.patch(f"{self.url}/{self.payload['pesel']}", json={"name": "John"})
        self.assertEqual(u_response.status_code, 200)
        self.assertEqual(u_response.json()["message"], "Account updated")

        response = requests.get(f"{self.url}/{self.payload['pesel']}")
        self.assertEqual(response.json()["name"], "John")

    @patch("requests.delete")
    def test_delete_account(self, mock_delete):
        print("Running test: Account Deletion (API)")

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Account deleted"}
        mock_delete.return_value = mock_response

        d_response = requests.delete(f"{self.url}/{self.payload['pesel']}")
        self.assertEqual(d_response.status_code, 200)
        self.assertEqual(d_response.json()["message"], "Account deleted")
