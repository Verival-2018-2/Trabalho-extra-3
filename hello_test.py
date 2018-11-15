import unittest
import sys
from hello_app import app


class HelloTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_root(self):
        converted_string = self.app.get('/').data.decode("utf-8") 
        assert 'Hello' in converted_string

if __name__ == '__main__':
    unittest.main()