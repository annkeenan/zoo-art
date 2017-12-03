import json
import requests
import unittest


class TestZoo(unittest.TestCase):
    PORT_NUM = '51042'
    print("Testing /zoo/")
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    ZOO_URL = SITE_URL + '/zoo/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        reqBody = {}
        r = requests.put(self.RESET_URL, data=json.dumps(reqBody))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_get_zoos(self):
        self.reset_data()
        r = requests.get(self.ZOO_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        zoo = resp['zoos']
        self.assertIsInstance(zoo, list)

    def test_get_zoo(self):
        self.reset_data()
        r = requests.get(self.ZOO_URL + 'Abilene_Zoo')
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['zoo'], {
            'city': 'Abilene',
            'state': 'TX',
            'address': '2070 Zoo Lane',
            'num_animals': 1100,
            'acres': 13,
            'opening_time': '9:00',
            'closing_time': '17:00',
            'annual_visitors': 175000,
            'website_url': 'http://abilenezoo.org/'
        })

    def test_put_zoo(self):
        self.reset_data()
        reqBody = {'annual_visitors': 15000}
        r = requests.put(self.ZOO_URL + 'Abilene_Zoo', data=json.dumps(reqBody))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.ZOO_URL + 'Abilene_Zoo')
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['zoo'], {
            'city': 'Abilene',
            'state': 'TX',
            'address': '2070 Zoo Lane',
            'num_animals': 1100,
            'acres': 13,
            'opening_time': '9:00',
            'closing_time': '17:00',
            'annual_visitors': 15000,
            'website_url': 'http://abilenezoo.org/'})

    def test_post_zoo(self):
        self.reset_data()
        reqBody = {
            'zoo': 'Fake_Zoo',
            'info': {
                'city': 'Anaheim',
                'state': 'CA',
                'address': '1234 Zoo Lane',
                'num_animals': 1700,
                'acres': 38,
                'opening_time': '8:00',
                'closing_time': '17:00',
                'annual_visitors': 185000,
                'website_url': 'http://fakezoo.org/'}}

        r = requests.post(self.ZOO_URL, data=json.dumps(reqBody))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        r = requests.get(self.ZOO_URL + 'Fake_Zoo')
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['zoo'], {
            'city': 'Anaheim',
            'state': 'CA',
            'address': '1234 Zoo Lane',
            'num_animals': 1700,
            'acres': 38,
            'opening_time': '8:00',
            'closing_time': '17:00',
            'annual_visitors': 185000,
            'website_url': 'http://fakezoo.org/'})


if __name__ == "__main__":
    unittest.main()
