from _zoo_database import _zoo_database
import unittest

class TestZooDatabase(unittest.TestCase):
    zdb = _zoo_database()

    def reset_database(self):
        self.zdb.reset_all()
        self.zdb.load_classification()
        self.zdb.load_exhibit()
        self.zdb.load_habitat()
        self.zdb.load_region()
        self.zdb.load_state()
        self.zdb.load_species()

    # Classification table tests
    def test_load_classification(self):
        self.reset_database()
        exp_result = {
            'Order': 'perciformes',
            'Class': 'actinopterygii',
            'Phylum': 'chordata',
            'Kingdom': 'animalia',
            'Desc': {'surgeonfish', 'tang', 'unicornfish'}
        }
        result = self.zdb.get_classication('acanthuridae')
        self.assertEquals(result, exp_result)

    # Exhibit table tests
    def test_get_exhibit(self):
        self.reset_database()
        exp_result = set(['aegolius acadicus', 'buteo jamaicensis', 'buteo lagopus', 'canis lupus', 'canis lupus familiaris',
            'cathartes aura', 'falco peregrinus', 'falco sparverius', 'haliaeetus leucocephalus', 'ursus arctos horribilis'])
        result = self.zdb.get_exhibit('Grizzly and Wolf Discovery Center')
        self.assertEquals(result, exp_result)
        
    def test_post_exhibit(self):
        self.reset_database()
        post_dict = {
            'zoo name': 'Blah Zoo',
            'species': set(['Kangaroo', 'Zebra'])
        }
        exp_result = set(['Kangaroo', 'Zebra']) 
        self.zdb.post_exhibit(post_dict)
        result = self.zdb.get_exhibit('Blah Zoo')
        self.assertEquals(result, exp_result)

    def test_delete_exhibit(self):
        self.reset_database()
        self.zdb.delete_exhibit('Birmingham Zoo')
        self.assertEquals(self.zdb.get_exhibit('Birmingham Zoo'), None)        
        
    # Habitat table tests
    def test_get_habitat(self):
        self.reset_database()
        exp_result = 'near the seabed at the bottom of a body of water'
        result = self.zdb.get_habitat('benthic')
        self.assertEquals(result, exp_result)

    # Region table tests
    def test_get_region(self):
        self.reset_database()
        exp_result = 'north america'
        result = self.zdb.get_region('nearctic')
        self.assertEquals(result, exp_result)

    # State table tests
    def test_get_state(self):
        self.reset_database()
        exp_result = 'North Carolina'
        result = self.zdb.get_state('NC')
        self.assertEquals(result, exp_result)

    def test_get_species(self):
        self.reset_database()
        exp_result = {
            'Common Name': set(['Blue-Throated Macaw', 'Caninde Macaw', 'Wagler\'s Macaw']),
            'Genus': 'ara',
            'Family': 'psittacidae',
            'Region': 'neotropical',
            'Habitat': set(['savanna/grassland', 'forest']),
            'Status': 'CR'
        }
        result = self.zdb.get_species('ara glaucogularis')
        self.assertEquals(result, exp_result)

    # Species table tests
    def test_put_species(self):
        self.reset_database()
        exp_result = {
            'Common Name': set(['Wagler\'s Macaw']),
            'Genus': 'fict',
            'Family': 'fict1',
            'Region': 'fict2',
            'Habitat': set(['savanna/grassland', 'fict']),
            'Status': 'LC'
        }
        self.zdb.put_species('ara glaucogularis', exp_result)
        result = self.zdb.get_species('ara glaucogularis')
        self.assertEquals(result, exp_result)

    def test_post_species(self):
        self.reset_database()
        post_dict = {
            'Species': 'Dire wolf', 
            'Common Name': set(['Dire wolf']),
            'Genus': 'Canis',
            'Family': 'Canidae',
            'Region': 'Westoros',
            'Habitat': set(['The North']),
            'Status': 'EX'
        }

        exp_result = {
            'Common Name': set(['Dire wolf']),
            'Genus': 'Canis',
            'Family': 'Canidae',
            'Region': 'Westoros',
            'Habitat': set(['The North']),
            'Status': 'EX'
        }
        self.zdb.post_species(post_dict)
        result = self.zdb.get_species('Dire wolf')
        self.assertEquals(result, exp_result)

    # Zoo Tests
    def test_put_zoo(self):
        self.reset_database()
        exp_result = {
            'City': 'Abilene',
            'State': 'TX',
            'Address': '1234 Test Lane',
            'Number of Animals': 420,
            'Acres': 69,
            'Opening Time': '9:00',
            'Closing Time': '17:00',
            'Annual Visitors': 175000,
            'Website URL': 'http://abilenezoo.org/'
        }           
        self.zdb.put_zoo('Audubon Zoo', exp_result)
        result = self.zdb.get_zoo('Audubon Zoo')
        self.assertEquals(result, exp_result)
    def test_post_zoo(self):
        self.reset_database()
        post_dict = {
            'Zoo': 'Hogwarts Zoo',
            'City': 'Yorba Linda',
            'State': 'CA',
            'Address': '1234 Zoo Lane',
            'Number of Animals': 777,
            'Acres': 19,
            'Opening Time': '9:00',
            'Closing Time': '17:00',
            'Annual Visitors': 45000,
            'Website URL': 'http://zoo.org/'
        }
        exp_result = {
            'City': 'Yorba Linda',
            'State': 'CA',
            'Address': '1234 Zoo Lane',
            'Number of Animals': 777,
            'Acres': 19,
            'Opening Time': '9:00',
            'Closing Time': '17:00',
            'Annual Visitors': 45000,
            'Website URL': 'http://zoo.org/'
        }
        self.zdb.post_zoo(post_dict)
        result = self.zdb.get_zoo('Hogwarts Zoo')
        self.assertEquals(result, exp_result)

    def test_get_zoo(self):
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
        result = self.zdb.get_zoo('Audubon Zoo')
        self.assertEquals(result, exp_result)    
    # Status Tests
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
