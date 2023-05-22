from lib.ec2_meta_data import retrive_local_ip, retrive_instance_id, retrive_public_ip
import json

class EC2Instance:
    def __init__(self, instance_id=None, local_ip=None, public_ip=None):
        self.instance_id = instance_id
        self.local_ip = local_ip
        self.public_ip = public_ip

    def to_list(self):
        return [
            {"title": "Instance ID", "value": self.instance_id},
            {"title": "Local IP", "value": self.local_ip},
            {"title": "Public IP", "value": self.public_ip}
        ]
    

class EC2Self(EC2Instance):
    def __init__(self):
        instance_id = retrive_instance_id()
        local_ip = retrive_local_ip()
        public_ip = retrive_public_ip()
        super().__init__(instance_id, local_ip, public_ip)


class EC2DB(EC2Instance):
    def __init__(self, instance_id=None, local_ip=None, public_ip=None, current=False):
        self.current = current
        super().__init__(instance_id, local_ip, public_ip)

    # convert the object to json string
    def to_json_string(self):
        return json.dumps(self.to_dict())

    # convert the object to dict
    def to_dict(self):
        return {
            "instance_id": self.instance_id,
            "local_ip": self.local_ip,
            "public_ip": self.public_ip,
            "current": self.current
        }

    # load the object from json string
    def load_from_json_string(self, json_string):
        json_object = json.loads(json_string)
        try:
            self.instance_id = json_object["instance_id"]
            self.local_ip = json_object["local_ip"]
            self.public_ip = json_object["public_ip"]
            self.current = json_object["current"]
        except:
            raise ValueError("json_string is not in the correct format")

