import json
import requests
import unittest


class TestExhibit(unittest.TestCase):
    PORT_NUM = '51042'
    print("Testing /species/")
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    SPECIES_URL = SITE_URL + '/species/'
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

    def test_get_all_species(self):
        self.reset_data()
        r = requests.get(self.SPECIES_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        species = resp['species']
        self.assertIsInstance(species, list)

    def test_get_species(self):
        self.reset_data()
        r = requests.get(self.SPECIES_URL + 'ara_glaucogularis')
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['ara_glaucogularis'], {
            'common_name': ['Blue-Throated Macaw', 'Caninde Macaw', 'Wagler\'s Macaw'],
            'genus': 'ara',
            'family': 'psittacidae',
            'region': ['neotropical'],
            'habitat': ['forest', 'savanna/grassland'],
            'status': 'CR'})

    def test_put_species(self):
        self.reset_data()
        reqBody = {}
        reqBody['status'] = 'EW'
        reqBody['habitat'] = ['rainforest']
        r = requests.put(self.SPECIES_URL + 'ara_glaucogularis',
                         data=json.dumps(reqBody))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.SPECIES_URL + 'ara_glaucogularis')
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['ara_glaucogularis'], {
            'common_name': ['Blue-Throated Macaw', 'Caninde Macaw', 'Wagler\'s Macaw'],
            'genus': 'ara',
            'family': 'psittacidae',
            'region': ['neotropical'],
            'habitat': ['forest', 'rainforest', 'savanna/grassland'],
            'status': 'EW'})

    def test_post_species(self):
        self.reset_data()
        reqBody = {}
        reqBody = {'species': 'canis_dirus', 'info': {
            'common_name': ['Dire wolf'],
            'genus': 'canis',
            'family': 'canidae',
            'region': ['holarctic'],
            'habitat': ['tundra'],
            'status': 'EX'}}

        r = requests.post(self.SPECIES_URL, data=json.dumps(reqBody))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        r = requests.get(self.SPECIES_URL + 'canis_dirus')
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['canis_dirus'], {
            'common_name': ['Dire wolf'],
            'genus': 'canis',
            'family': 'canidae',
            'region': ['holarctic'],
            'habitat': ['tundra'],
            'status': 'EX'})


if __name__ == "__main__":
    unittest.main()
