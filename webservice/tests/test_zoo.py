import json
import requests
import unittest


class TestZoo(unittest.TestCase):
	PORT_NUM = '51068'
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
		zoo = resp['zoo']
		self.assertIsInstance(zoo, list)

	def test_get_zoo(self):
		self.reset_data()
		r = requests.get(self.ZOO_URL + 'Abilene Zoo')
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		self.assertEqual(resp['Abilene Zoo'],
            {'city': 'Abilene',
            'state': 'TX',
            'address': '2070 Zoo Lane',
            'number of animals': 1100,
            'acres': 13,
            'opening time': '9:00',
            'closing time': '17:00',
            'annual visitors': 175000,
            'website URL': 'http://abilenezoo.org/'}
        )

	def test_put_zoo(self):
		self.reset_data()
		reqBody = {}
		reqBody['annual visitors'] = 15000
		r = requests.put(self.ZOO_URL + 'Abilene Zoo', data=json.dumps(reqBody))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.ZOO_URL + 'Abilene Zoo')
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		self.assertEqual(resp['Abilene Zoo'],
            {'city': 'Abilene',
            'state': 'TX',
            'address': '2070 Zoo Lane',
            'number of animals': 1100,
            'acres': 13,
            'opening time': '9:00',
            'closing time': '17:00',
            'annual visitors': 15000,
            'website URL': 'http://abilenezoo.org/'}
        )

	def test_post_zoo(self):
		self.reset_data()
		reqBody = {}
		reqBody = {'zoo': 'Fake Zoo',
            'info': {
            'city': 'Anaheim',
            'state': 'Ca',
            'address': '1234 Zoo Lane',
            'number of animals': 1700,
            'acres': 38,
            'opening time': '8:00',
            'closing time': '17:00',
            'annual visitors': 185000,
            'website URL': 'http://fakezoo.org/'
            }}


		r = requests.post(self.ZOO_URL, data=json.dumps(reqBody))
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		r = requests.get(self.ZOO_URL + 'Fake Zoo')
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['result'], 'success')
		self.assertEqual(resp['Fake Zoo'], {
            'city': 'Anaheim',
            'state': 'Ca',
            'address': '1234 Zoo Lane',
            'number of animals': 1700,
            'acres': 38,
            'opening time': '8:00',
            'closing time': '17:00',
            'annual visitors': 185000,
            'website URL': 'http://fakezoo.org/'
            }
)



if __name__ == "__main__":
    unittest.main()
