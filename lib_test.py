import unittest
from lib import abc

class TestLib(unittest.TestCase):

    def test_abc(self):
        # Test case for abc function
        result = abc()
        self.assertEqual(result, "Hello from lib.py!")

if __name__ == "__main__":
    unittest.main()