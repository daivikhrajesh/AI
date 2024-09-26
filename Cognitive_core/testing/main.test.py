import unittest
from fastapi.testclient import TestClient
from app.api.app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_read_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to Cognitive CORE API"})

    def test_process(self):
        response = self.client.post("/process/", json={"data": "Sample input"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("evaluation", response.json())

if __name__ == "__main__":
    unittest.main()
