from client import create_message
import unittest
import time

class TestServer(unittest.TestCase):

    def test_create_message(self):
        action = "presence"
        time_s = time.ctime(time.time())
        type_s = "status"

        self.assertTrue(create_message(action, time_s, type_s), {
            "action": action,
            "time": time_s,
            "type": type_s,
        })

if(__name__ == "__main__"):
    unittest.main()