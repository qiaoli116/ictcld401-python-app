import unittest
import re
from models.ec2_meta_data import EC2MetaData
class EC2MetaDataUnitTest(unittest.TestCase):
    def test_retrive_local_ip(self):
        result = EC2MetaData.retrive_local_ip()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertTrue(self.is_valid_ipv4_address(result))

    def test_retrive_instance_id(self):
        result = EC2MetaData.retrive_instance_id()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)

    def test_retrive_public_ip(self):
        result = EC2MetaData.retrive_public_ip()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertTrue(self.is_valid_ipv4_address(result))

    def is_valid_ipv4_address(self, address):
        # Regular expression pattern for IPv4 address
        pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
        return re.match(pattern, address) is not None

if __name__ == "__main__":
    unittest.main()
