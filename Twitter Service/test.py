import unittest
from local_config import *
from app import app

class TweepyTestCase(unittest.TestCase):

    def test_app(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.content_type, "text/html; charset=utf-8")

if __name__ == "__main__":
    unittest.main()


# Reference code by soumilshah1995 from youtube