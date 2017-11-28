import json
import requests
import unittest


class TestClassification(unittest.TestCase):
    PORT_NUM = '51042'
    print("Testing port number: ", PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    CLASSIFICATION_URL = SITE_URL + '/classification/'
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

    def test_get_families(self):
        self.reset_data()
        # Get the server response
        r = requests.get(self.CLASSIFICATION_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        # Check the response
        self.assertEqual(resp['result'], 'success')
        self.assertIsInstance(resp['families'], list)

    def test_get_classification(self):
        self.reset_data()
        # Get the server response
        r = requests.get(self.CLASSIFICATION_URL + 'acanthuridae')
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        # Check the response
        self.assertEqual(resp['result'], 'success')
        classification = resp['classification']
        self.assertEqual(classification['order'], 'perciformes')
        self.assertEqual(classification['class'], 'actinopterygii')
        self.assertEqual(classification['phylum'], 'chordata')
        self.assertEqual(classification['kingdom'], 'animalia')
        self.assertCountEqual(classification['desc'], ['surgeonfish', 'tang', 'unicornfish'])

    def test_post_classification(self):
        self.reset_data()
        # Build the input dictionary
        m = {}
        m['family'] = 'test'
        m['info'] = {
            'order': 'order',
            'class': 'class',
            'phylum': 'phylum',
            'kingdom': 'kingdom',
            'desc': ['desc1', 'desc2']
        }
        # Post the request to the server
        r = requests.post(self.CLASSIFICATION_URL, data=json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        # Check the response
        self.assertEqual(resp['result'], 'success')


if __name__ == "__main__":
    unittest.main()
