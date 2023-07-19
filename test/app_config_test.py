import unittest
# from app_config import app_config 
from models.config import AppConfig 


class AppConfigTest(unittest.TestCase):
    config_file_template = "config_template.ini"
    config_file_successful = "config.ini"
    def test_app_config_01_server_config_host(self):
        app_config = AppConfig(AppConfigTest.config_file_successful)
        print(app_config.server_config.host)
        self.assertIsInstance(app_config.server_config.host, str)
        

    def test_app_config_02_server_config_port(self):
        app_config = AppConfig(AppConfigTest.config_file_successful)
        print(app_config.server_config.port)
        self.assertIsInstance(app_config.server_config.port, int)

    def test_app_config_03_static_base_url(self):
        app_config = AppConfig(AppConfigTest.config_file_successful)
        print(app_config.static_config.base_url)
        self.assertIsInstance(app_config.static_config.base_url, str)

    def test_app_config_04_db_static_is_up(self):
        app_config = AppConfig(AppConfigTest.config_file_successful)
        print(app_config.static_config.is_base_url_up())
        self.assertIsInstance(app_config.static_config.is_base_url_up(), bool)

    def test_app_config_05_db_config_endpoint(self):
        app_config = AppConfig(AppConfigTest.config_file_successful)
        print(f"[{app_config.db_config.endpoint}]")
        self.assertIsInstance(app_config.db_config.endpoint, str)

    def test_app_config_06_db_config_port(self):
        app_config = AppConfig(AppConfigTest.config_file_successful)
        print(app_config.db_config.port)
        self.assertIsInstance(app_config.db_config.port, int)
    
    def test_app_config_07_db_config_user(self):
        app_config = AppConfig(AppConfigTest.config_file_successful)
        print(app_config.db_config.user)
        self.assertIsInstance(app_config.db_config.user, str)

    def test_app_config_08_db_config_password(self):
        app_config = AppConfig(AppConfigTest.config_file_successful)
        print(app_config.db_config.password)
        self.assertIsInstance(app_config.db_config.password, str)

    def test_app_config_09_db_config_database(self):
        app_config = AppConfig(AppConfigTest.config_file_successful)
        print(app_config.db_config.database)
        self.assertIsInstance(app_config.db_config.database, str)

    def test_app_config_10_db_config_table(self):
        app_config = AppConfig(AppConfigTest.config_file_successful)
        print(app_config.db_config.table)
        self.assertIsInstance(app_config.db_config.table, str)

    def test_app_config_20_save_server_config_host(self):
        app_config = AppConfig(AppConfigTest.config_file_successful)
        host = "192.168.0.1"
        app_config.save_configuration_server_host(host)
        app_config.load_configuration()
        self.assertEqual(app_config.server_config.host, host)
        AppConfig.reset_configuration(AppConfigTest.config_file_template, AppConfigTest.config_file_successful)

    def test_app_config_21_save_server_config_port(self):
        app_config = AppConfig(AppConfigTest.config_file_successful)
        port = 8080
        app_config.save_configuration_server_port(port)
        app_config.load_configuration()
        self.assertEqual(app_config.server_config.port, port)
        port = "8080"
        app_config.save_configuration_server_port(port)
        app_config.load_configuration()
        port = 8080
        self.assertEqual(app_config.server_config.port, port)
        port = "8080abc"
        app_config.save_configuration_server_port(port)
        app_config.load_configuration()
        port = 0
        self.assertEqual(app_config.server_config.port, port)
        AppConfig.reset_configuration(AppConfigTest.config_file_template, AppConfigTest.config_file_successful)
    
    def test_app_config_22_save_static_config_base_url(self):
        app_config = AppConfig(AppConfigTest.config_file_successful)
        base_url = "http://abc.com/"
        app_config.save_configuration_static_base_url(base_url)
        app_config.load_configuration()
        base_url = "http://abc.com"
        self.assertEqual(app_config.static_config.base_url, base_url)
        AppConfig.reset_configuration(AppConfigTest.config_file_template, AppConfigTest.config_file_successful)

    def test_app_config_23_save_db_config_endpoint(self):
        app_config = AppConfig(AppConfigTest.config_file_successful)
        endpoint = "localhost"
        app_config.save_configuration_db_endpoint(endpoint)
        app_config.load_configuration()
        self.assertEqual(app_config.db_config.endpoint, endpoint)
        AppConfig.reset_configuration(AppConfigTest.config_file_template, AppConfigTest.config_file_successful)

    def test_app_config_24_save_db_config_port(self):
        app_config = AppConfig(AppConfigTest.config_file_successful)
        port = 3306
        app_config.save_configuration_db_port(port)
        app_config.load_configuration()
        self.assertEqual(app_config.db_config.port, port)
        AppConfig.reset_configuration(AppConfigTest.config_file_template, AppConfigTest.config_file_successful)
    
    def test_app_config_25_save_db_config_user(self):
        app_config = AppConfig(AppConfigTest.config_file_successful)
        user = "abc"
        app_config.save_configuration_db_user(user)
        app_config.load_configuration()
        self.assertEqual(app_config.db_config.user, user)
        AppConfig.reset_configuration(AppConfigTest.config_file_template, AppConfigTest.config_file_successful)

    def test_app_config_26_save_db_config_password(self):
        app_config = AppConfig(AppConfigTest.config_file_successful)
        password = "abc"
        app_config.save_configuration_db_password(password)
        app_config.load_configuration()
        self.assertEqual(app_config.db_config.password, password)
        AppConfig.reset_configuration(AppConfigTest.config_file_template, AppConfigTest.config_file_successful)


if __name__ == "__main__":
    unittest.main()
