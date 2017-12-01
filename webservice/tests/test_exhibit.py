import json
import requests
import unittest


class TestExhibit(unittest.TestCase):
    PORT_NUM = '51042'
    print("Testing /exibit/")
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    EXHIBIT_URL = SITE_URL + '/exhibit/'
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

    def test_get_exhibits(self):
        self.reset_data()
        r = requests.get(self.EXHIBIT_URL +
                         'Grizzly and Wolf Discovery Center')
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        exhibits = resp['species']
        self.assertEqual(exhibits, [
            'aegolius acadicus',
            'buteo jamaicensis',
            'buteo lagopus',
            'canis lupus',
            'canis lupus familiaris',
            'cathartes aura',
            'falco peregrinus',
            'falco sparverius',
            'haliaeetus leucocephalus',
            'ursus arctos horribilis',
        ])

    def test_post_exhibit(self):
        self.reset_data()
        reqBody = {}
        reqBody['species'] = ['acanthurus olivaceus', 'acanthurus pyroferus']
        r = requests.post(
            self.EXHIBIT_URL + 'Grizzly and Wolf Discovery Center', data=json.dumps(reqBody))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.EXHIBIT_URL +
                         'Grizzly and Wolf Discovery Center')
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['species'], [
            'acanthurus olivaceus',
            'acanthurus pyroferus',
            'aegolius acadicus',
            'buteo jamaicensis',
            'buteo lagopus',
            'canis lupus',
            'canis lupus familiaris',
            'cathartes aura',
            'falco peregrinus',
            'falco sparverius',
            'haliaeetus leucocephalus',
            'ursus arctos horribilis',
        ])

    def test_delete_exhibit(self):
        self.reset_data()
        r = requests.delete(
            self.EXHIBIT_URL + 'Grizzly and Wolf Discovery Center' + '/haliaeetus leucocephalus')
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        r = requests.get(self.EXHIBIT_URL +
                         'Grizzly and Wolf Discovery Center')
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['species'], [
            'aegolius acadicus',
            'buteo jamaicensis',
            'buteo lagopus',
            'canis lupus',
            'canis lupus familiaris',
            'cathartes aura',
            'falco peregrinus',
            'falco sparverius',
            'ursus arctos horribilis',
        ])


if __name__ == "__main__":
    unittest.main()
