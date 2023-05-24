import unittest
from app_config import app_config 

class AppConfigTest(unittest.TestCase):
    def test_app_config_01_server_config_host(self):
        print(app_config.server_config.host)
        self.assertIsInstance(app_config.server_config.host, str)

    def test_app_config_02_server_config_port(self):
        print(app_config.server_config.port)
        self.assertIsInstance(app_config.server_config.port, int)

    def test_app_config_03_static_base_url(self):
        print(app_config.static_config.base_url)
        self.assertIsInstance(app_config.static_config.base_url, str)

    def test_app_config_04_db_static_is_up(self):
        print(app_config.static_config.is_base_url_up())
        self.assertIsInstance(app_config.static_config.is_base_url_up(), bool)

    def test_app_config_05_db_config_endpoint(self):
        print(f"[{app_config.db_config.endpoint}]")
        self.assertIsInstance(app_config.db_config.endpoint, str)

    def test_app_config_06_db_config_port(self):
        print(app_config.db_config.port)
        self.assertIsInstance(app_config.db_config.port, int)
    
    def test_app_config_07_db_config_user(self):
        print(app_config.db_config.user)
        self.assertIsInstance(app_config.db_config.user, str)

    def test_app_config_08_db_config_password(self):
        print(app_config.db_config.password)
        self.assertIsInstance(app_config.db_config.password, str)

    def test_app_config_09_db_config_database(self):
        print(app_config.db_config.database)
        self.assertIsInstance(app_config.db_config.database, str)

    def test_app_config_10_db_config_table(self):
        print(app_config.db_config.table)
        self.assertIsInstance(app_config.db_config.table, str)

if __name__ == "__main__":
    unittest.main()
