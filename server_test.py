from server import create_message
import unittest

class TestServer(unittest.TestCase):

    def test_create_message(self):
        text = "Hello world"
        code = 200

        self.assertTrue(create_message(text, code), {
            "response": code,
            "alert": text
        })

if(__name__ == "__main__"):
    unittest.main()