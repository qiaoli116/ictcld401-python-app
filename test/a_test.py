import unittest
from lib.abc import abc

class TestLib(unittest.TestCase):

    def test_abc1(self):
        # Test case for abc function
        result = abc()
        # print(result)
        self.assertEqual(result, "Hello frbc function!")

    def test_abc2(self):
        # Test case for abc function
        result = abc()
        # print(result)
        self.assertEqual(result, "Hello from abc function!")

    def test_abc3(self):
        # Test case for abc function
        result = abc()
        # print(result)
        self.assertEqual(result, "Hello from abc function!")

if __name__ == "__main__":
    unittest.main()