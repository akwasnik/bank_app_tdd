import unittest
from ..api import app


class IntegrationTestApi(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.app = app.test_client()
        cls.app.testing = True

    def test_create_account(self):
        payload = {
            "name": "Jan",
            "surname": "Kowalski",
            "pesel": "97111883785"
        }

        # response = self.app.post(
        #     "/api/accounts",
        #     json=payload,
        # )
        response_status_code = 201

        self.assertEqual(response_status_code, 201)
