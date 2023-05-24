import unittest
from app_config import app_config
from models.db import AppDAL
from models.ec2_instance import EC2DBItem
import json

class DBTest(unittest.TestCase):
    def init_app_dal(self):
        return AppDAL(
            host=app_config.db_config.endpoint,
            port=app_config.db_config.port,
            user=app_config.db_config.user,
            password=app_config.db_config.password,
            database=app_config.db_config.database,
            table=app_config.db_config.table
        )

    # def test_app_04_create_item(self):
    #     app_dal = self.init_app_dal()
    #     app_dal.connect_to_sql_server()
    #     result = app_dal.connect_to_db()

    #     if result:
    #         item = EC2DBItem(
    #             instance_id=retrive_instance_id(),
    #             local_ip=retrive_local_ip(),
    #             public_ip=retrive_public_ip(),
    #             app_port=app_config.server_config.port,
    #         )
    #         app_dal.create_item(item.instance_id, json.dumps(item.to_dict_db()))
    #         # for loop run 5 times
    #         for i in range(5):
    #             item = EC2DBItem(
    #                 instance_id=f"i-0000000000000000{i}",
    #                 local_ip=f"192.168.0.{i}",
    #                 public_ip=f"3.0.0.{i}",
    #                 app_port=app_config.server_config.port,
    #             )
    #             app_dal.create_item(item.instance_id, json.dumps(item.to_dict_db()))

    #     else:
    #         print("Failed to connect to database")
    #     app_dal.close_connection()

    # def test_app_05_read_all_items(self):
    #     app_dal = self.init_app_dal()
    #     app_dal.connect_to_sql_server()
    #     result = app_dal.connect_to_db()

    #     if result:
    #         items = app_dal.read_all_items()
    #         print(f"Total items: {len(items)}")
    #         for item in items:
    #             print(item)
    #     else:
    #         print("Failed to connect to database")
    #     app_dal.close_connection()

    # def test_app_06_read_one_item_found(self):
    #     app_dal = self.init_app_dal()
    #     app_dal.connect_to_sql_server()
    #     result = app_dal.connect_to_db()

    #     if result:
    #         item = app_dal.read_one_item("i-03c31c34d358e4fc9")
    #         print(item)
    #     else:
    #         print("Failed to connect to database")
    #     app_dal.close_connection()

    # def test_app_07_read_one_item_not_found(self):
    #     app_dal = self.init_app_dal()
    #     app_dal.connect_to_sql_server()
    #     result = app_dal.connect_to_db()

    #     if result:
    #         item = app_dal.read_one_item("i-03c31c34d358e111")
    #         print(item)
    #     else:
    #         print("Failed to connect to database")
    #     app_dal.close_connection()

    # # def test_app_07_delete_item(self):
    # #     app_dal = self.init_app_dal()
    # #     app_dal.connect_to_sql_server()
    # #     result = app_dal.connect_to_db()

    # #     if result:
    # #         app_dal.delete_item("i-00000000000000001")
    # #     else:
    # #         print("Failed to connect to database")
    # #     app_dal.close_connection()

    # def test_app_10_retrieve_public_ip_found(self):
    #     app_dal = self.init_app_dal()
    #     app_dal.connect_to_sql_server()
    #     result = app_dal.connect_to_db()

    #     if result:
    #         public_ip = app_dal.retrieve_public_ip("i-03c31c34d358e4fc9")
    #         print(f"public ip: {public_ip}")
    #     else:
    #         print("Failed to connect to database")
    #     app_dal.close_connection()

    # def test_app_11_retrieve_public_ip_not_found(self):
    #     app_dal = self.init_app_dal()
    #     app_dal.connect_to_sql_server()
    #     result = app_dal.connect_to_db()

    #     if result:
    #         public_ip = app_dal.retrieve_public_ip("i-03c31c34d3500000")
    #         print(f"public ip: {public_ip}")
    #     else:
    #         print("Failed to connect to database")
    #     app_dal.close_connection()

    # def test_app_12_is_website_public_ip_up_true(self):
    #     app_dal = self.init_app_dal()
    #     app_dal.connect_to_sql_server()
    #     result = app_dal.connect_to_db()

    #     if result:
    #         print(app_dal.is_website_public_ip_up("i-0415dc1b275876158", 8080))
    #     else:
    #         print("Failed to connect to database")
    #     app_dal.close_connection()

    # def test_app_13_is_website_public_ip_up_false_1(self):
    #     app_dal = self.init_app_dal()
    #     app_dal.connect_to_sql_server()
    #     result = app_dal.connect_to_db()

    #     if result:
    #         print(app_dal.is_website_public_ip_up("i-121212121", 8080))
    #     else:
    #         print("Failed to connect to database")
    #     app_dal.close_connection()

    def test_app_14_is_website_public_ip_up_false_2(self):
        app_dal = self.init_app_dal()
        app_dal.connect_to_sql_server()
        result = app_dal.connect_to_db()

        if result:
            print(app_dal.is_website_public_ip_up(instance_id="i-0415dc1b275876158", public_ip="3.81.231.198", app_port=8080))
        else:
            print("Failed to connect to database")
        app_dal.close_connection()

    # def test_app_15_retrieve_all_public_ip(self):
    #     app_dal = self.init_app_dal()
    #     app_dal.connect_to_sql_server()
    #     result = app_dal.connect_to_db()
    #     if result:
    #         public_ips = app_dal.retrieve_all_public_ip()
    #         print(public_ips)
    #     else:
    #         print("Failed to connect to database")
    #     app_dal.close_connection()

    # def test_app_16_update_app_db(self):
    #     app_dal = self.init_app_dal()
    #     app_dal.connect_to_sql_server()
    #     result = app_dal.connect_to_db()
    #     if result:
    #         app_dal.update_app_db()
    #         print("Update app db successfully")
    #         print(app_dal.read_all_items())
    #         print("read all data")
    #     else:
    #         print("Failed to connect to database")
    #     app_dal.close_connection()

if __name__ == "__main__":
    unittest.main()
