import json
import requests
import unittest


class TestRegion(unittest.TestCase):
    PORT_NUM = '51068'
    print("Testing /status/")
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    STATUS_URL = SITE_URL + '/status/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        m = {}
        r = requests.put(self.RESET_URL, data=json.dumps(m))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_get_statuses(self):
        self.reset_data()
        # Get the server response
        r = requests.get(self.STATUS_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        # Check the response
        self.assertEqual(resp['result'], 'success')
        self.assertIsInstance(resp['statuses'], list)

    def test_get_status(self):
        self.reset_data()
        # Get the server response
        r = requests.get(self.STATUS_URL + 'DD')
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        # Check the response
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['description'], 'data deficient')

if __name__ == "__main__":
    unittest.main()
