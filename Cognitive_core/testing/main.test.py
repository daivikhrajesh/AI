import unittest
from app.main import process_user_input

class MyTestCase(unittest.TestCase):
    def test_process_user_input(self):
        result = process_user_input("What is AI?")
        self.assertIn("evaluated", result)  # Change based on expected output structure

if __name__ == '__main__':
    unittest.main()
