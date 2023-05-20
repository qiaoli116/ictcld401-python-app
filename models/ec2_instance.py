from lib.ec2_meta_data import retrive_local_ip, retrive_instance_id, retrive_public_ip

class EC2Instance:
    def __init__(self, instance_id=None, local_ip=None, public_ip=None):
        self.instance_id = instance_id
        self.local_ip = local_ip
        self.public_ip = public_ip

    def ToList(self):
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
