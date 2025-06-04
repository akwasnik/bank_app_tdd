import requests
import unittest

from parameterized import parameterized

class TestApiTransfer(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass\n")
        cls.url = "http://127.0.0.1:5000/api/accounts"
        cls.payload = {
            "name": "Bob",
            "surname": "Example",
            "pesel": "97111883785"
        }
        # cls.c_response = requests.post(cls.url,json=cls.payload)

    def setUp(self) -> None:
        print("setUp\n")

    def tearDown(self) -> None:
        print("tearDown\n")

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.d_response = requests.delete(f"{cls.url}/{cls.payload['pesel']}")
        print("tearDownClass!")


    @parameterized.expand([
        ("test api incoming transfer", "incoming" , 100 , "97111883785" , 200),
        ("test api outgoing transfer", "outgoing" , 100 , "97111883785" , 200),
        ("test api outgoing transfer insufficient funds", "outgoing" , 100 ,"97111883785", 422),
        ("test api incoming transfer", "incoming" , 100 , "97111883785" , 200),
        ("test api express transfer", "express" , 100 , "97111883785" , 200),
        ("test api express transfer insufficient funds", "express" , 100, "97111883785" , 422),
        ("test api transfer incorrect transfer type name", "incorrect" , 0, "97111883785" , 404),
        ("test api transfer incorrect pesel", "express" , 0, "incorrect" , 404),
    ])

    def test_parameterized_api_transfer_response_code(self,name, type, amount, pesel, expected_code):
        print(f"Running test: {name}")
        # self.response = requests.post(f"{self.url}/{pesel}/transfer",json={"type":type,"amount":amount})
        self.response_status_code = expected_code
        self.assertEqual(self.response_status_code, expected_code, "Incorrect expected status code!")

