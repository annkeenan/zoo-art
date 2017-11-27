from _zoo_database import _zoo_database
import unittest

class TestZooDatabase(unittest.TestCase):
    zdb = _zoo_database()

    def reset_database(self):
        self.zdb.reset_all()

    def test_load_classification(self):
        self.reset_database()
        exp_result = {
            'Order': 'perciformes',
            'Class': 'actinopterygii',
            'Phylum': 'chordata',
            'Kingdom': 'animalia',
            'Desc': {'surgeonfish', 'tang', 'unicornfish'}
        }
        self.zdb.load_classification()
        result = self.zdb.get_classication('acanthuridae')
        self.assertEquals(result, exp_result)

    def test_load_habitat(self):
        self.reset_database()
        exp_result = 'near the seabed at the bottom of a body of water'
        self.zdb.load_habitat()
        result = self.zdb.get_habitat('benthic')
        self.assertEquals(result, exp_result)

    def test_load_region(self):
        self.reset_database()
        exp_result = 'north america'
        self.zdb.load_region()
        result = self.zdb.get_region('nearctic')
        self.assertEquals(result, exp_result)

    def test_load_state(self):
        self.reset_database()
        exp_result = 'North Carolina'
        self.zdb.load_state()
        result = self.zdb.get_state('NC')
        self.assertEquals(result, exp_result)

    def test_load_species(self):
        self.reset_database()
        exp_result = {
            'Common Name': set(['Blue-Throated Macaw', 'Caninde Macaw', 'Wagler\'s Macaw']),
            'Genus': 'ara',
            'Family': 'psittacidae',
            'Region': 'neotropical',
            'Habitat': set(['savanna/grassland', 'forest']),
            'Status': 'CR'
        }
        self.zdb.load_species()
        result = self.zdb.get_species('ara glaucogularis')
        self.assertEquals(result, exp_result)

    def test_load_exhibit(self):
        self.reset_database()
        exp_result = set(['aegolius acadicus', 'buteo jamaicensis', 'buteo lagopus', 'canis lupus', 'canis lupus familiaris',
            'cathartes aura', 'falco peregrinus', 'falco sparverius', 'haliaeetus leucocephalus', 'ursus arctos horribilis'])
        self.zdb.load_exhibit()
        result = self.zdb.get_exhibit('Grizzly and Wolf Discovery Center')
        self.assertEquals(result, exp_result)
    def test_load_zoo(self):
        self.reset_database()
        exp_result = {
            'City': 'Abilene',
            'State': 'TX',
            'Address': '2070 Zoo Lane',
            'Number of Animals': 1100,
            'Acres': 13,
            'Opening Time': '9:00',
            'Closing Time': '17:00',
            'Annual Visitors': 175000,
            'Website URL': 'http://abilenezoo.org/'
        }
        self.zdb.load_zoo()
        result = self.zdb.get_zoo('Audubon Zoo')
        self.assertEquals(result, exp_result)    
           
    def test_load_status(self):
        self.reset_database()
        exp_result = {
            'Level': 0,
            'Description': 'data deficient'
        }
        self.zdb.load_status()
        result = self.zdb.get_status('DD')
        self.assertEquals(result, exp_result)


if __name__ == "__main__":
    unittest.main()
