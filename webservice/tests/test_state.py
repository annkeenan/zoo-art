import json
import requests
import unittest


class TestExhibit(unittest.TestCase):
	PORT_NUM = '51056'
	print("Testing /state/")
	SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
	STATE_URL = SITE_URL + '/state/'
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

	def test_get_states(self):
		self.reset_data()
		r = requests.get(self.STATE_URL)
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertIsInstance(resp['states'], list)

	def test_get_state(self):
		self.reset_data()
		r = requests.get(self.STATE_URL + 'AZ')
		self.assertTrue(self.is_json(r.content.decode()))
		resp = json.loads(r.content.decode())
		self.assertEqual(resp['state'], 'Arizona')


if __name__ == "__main__":
    unittest.main()
