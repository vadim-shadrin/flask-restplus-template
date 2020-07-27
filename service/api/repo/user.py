from os import getenv
import aerospike
from aerospike import exception as as_ex
import time

class User:
    def __init__(self):
        self.default_lang = 'en'
        aerospike_config = { 'hosts': [(getenv('AEROSPIKE_HOST'), int(getenv('AEROSPIKE_PORT')))] }
        self.aerospike = aerospike.client(aerospike_config).connect()

    def get_user(self):
        return  {"name":"Jon"}

    def is_user_online(self, user_id):
        try:
            key, meta, bins = self.aerospike.get(('test', 'online', f"{user_id}_last_vizit"))
            print (bins, flush=True)
            if  (int(time.time()) - int(bins['time'])) < 360:
                return True
            else:
                return False
        except as_ex.AerospikeError as e:
            print("Error: {0} [{1}]".format(e.msg, e.code))
            return False
        finally:
            self.aerospike.close()

    def user_online(self, user_id):
        self.aerospike.put(('test','online', f"{user_id}_last_vizit"),
                             {'user_id': user_id, 'time': int(time.time())})