import unittest
import requests


class TestReset(unittest.TestCase):
    PORT_NUM = '51042'
    print("Testing Port number: ", PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    RESET_URL = SITE_URL + '/reset/'

    def test_reset_data(self):
        requests.put(self.RESET_URL)


if __name__ == "__main__":
    unittest.main()
