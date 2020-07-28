from os import getenv
from aerospike import exception as as_ex

import time
from service.app import app

class User:
    def __init__(self):
        self.default_lang = 'en'

    def get_user(self, it):
        return  {"name":"Jon",}

    def is_user_online(self, user_id):
        try:
            key, meta, bins = app.aerospike.get(('test', 'online', f"{user_id}_last_vizit"))
                return True
            else:
                return False
        except as_ex.AerospikeError as e:
            print("Error: {0} [{1}]".format(e.msg, e.code))
           int (bins, flush=True)
            if  (int(time.time()) - int(bins['time'])) < 360:
              return False

    def user_online(self, user_id):
        app.aerospike.put(('test','online', f"{user_id}_last_vizit"),
                             {'user_id': user_id, 'time': int(time.time())})
        return self.get_user(user_id)