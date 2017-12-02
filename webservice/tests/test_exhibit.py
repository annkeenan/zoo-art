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

    def test_get_exhibits_zoo(self):
        self.reset_data()
        r = requests.get(self.EXHIBIT_URL + 'Grizzly_and_Wolf_Discovery_Center' + '/true')
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        exhibits = resp['species']
        self.assertEqual(exhibits, [
            'aegolius_acadicus',
            'buteo_jamaicensis',
            'buteo_lagopus',
            'canis_lupus',
            'canis_lupus_familiaris',
            'cathartes_aura',
            'falco_peregrinus',
            'falco_sparverius',
            'haliaeetus_leucocephalus',
            'ursus_arctos_horribilis'
        ])

    def test_get_not_exhibited_zoo(self):
        self.reset_data()
        r = requests.get(self.EXHIBIT_URL + 'Grizzly_and_Wolf_Discovery_Center' + '/false')
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        exhibits = resp['species']
        self.assertIsInstance(exhibits, list)

    def test_get_exhibits_species(self):
        self.reset_data()
        r = requests.get(self.EXHIBIT_URL + 'bison_bison')
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        zoos = resp['zoos']
        self.assertEqual(zoos,[
            'Baton_Rouge_Zoo',
            'Bronx_Zoo',
            'Brookfield_Zoo',
            'Chahinkapa_Zoo',
            'Connecticuts_Beardsley_Zoo',
            'Fossil_Rim_Wildlife_Center',
            'Great_Plains_Zoo',
            'Minnesota_Zoo',
            'North_Carolina_Zoo',
            'Potawatomi_Zoo'])
	    
    def test_post_exhibit(self):
        self.reset_data()
        reqBody = {}
        reqBody['species'] = ['acanthurus_olivaceus', 'acanthurus_pyroferus']
        r = requests.post(self.EXHIBIT_URL + 'Grizzly_and_Wolf_Discovery_Center', data=json.dumps(reqBody))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.EXHIBIT_URL +
                         'Grizzly_and_Wolf_Discovery_Center' + '/true')
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['species'], [
            'acanthurus_olivaceus',
            'acanthurus_pyroferus',
            'aegolius_acadicus',
            'buteo_jamaicensis',
            'buteo_lagopus',
            'canis_lupus',
            'canis_lupus_familiaris',
            'cathartes_aura',
            'falco_peregrinus',
            'falco_sparverius',
            'haliaeetus_leucocephalus',
            'ursus_arctos_horribilis'
        ])

    def test_delete_exhibit(self):
        self.reset_data()
        r = requests.delete(
            self.EXHIBIT_URL + 'Grizzly_and_Wolf_Discovery_Center' + '/haliaeetus_leucocephalus')
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        r = requests.get(self.EXHIBIT_URL +
                         'Grizzly_and_Wolf_Discovery_Center' + '/true')
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['species'], [
            'aegolius_acadicus',
            'buteo_jamaicensis',
            'buteo_lagopus',
            'canis_lupus',
            'canis_lupus_familiaris',
            'cathartes_aura',
            'falco_peregrinus',
            'falco_sparverius',
            'ursus_arctos_horribilis'
        ])


if __name__ == "__main__":
    unittest.main()
