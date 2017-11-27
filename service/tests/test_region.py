import json
import requests
import unittest


class TestRegion(unittest.TestCase):
    PORT_NUM = '51042'
    print("Testing port number: ", PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    REGION_URL = SITE_URL + '/region/'
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

    def test_get_regions(self):
        self.reset_data()
        # Get the server response
        r = requests.get(self.REGION_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        # Check the response
        self.assertEqual(resp['result'], 'success')
        self.assertIsInstance(resp['regions'], list)

    def test_get_region(self):
        self.reset_data()
        # Get the server response
        r = requests.get(self.REGION_URL + 'nearctic')
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        # Check the response
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['desc'], 'north america')

    def test_post_region(self):
        self.reset_data()
        # Build the input dictionary
        m = {}
        m['region'] = 'region'
        m['desc'] = 'desc'
        # Post the request to the server
        r = requests.post(self.REGION_URL, data=json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        # Check the response
        self.assertEqual(resp['result'], 'success')


if __name__ == "__main__":
    unittest.main()
