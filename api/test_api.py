from _zoo_database import _zoo_database
import unittest

class TestZooDatabase(unittest.TestCase):
    zdb = _zoo_database()

    def reset_database(self):
        self.zdb.reset_all()
        self.zdb.load_all()

## Classification table tests
    def test_get_classification(self):
        self.reset_database()
        exp_result = {
            'Order': 'perciformes',
            'Class': 'actinopterygii',
            'Phylum': 'chordata',
            'Kingdom': 'animalia',
            'Desc': {'surgeonfish', 'tang', 'unicornfish'}
        }
        result = self.zdb.get_classication('acanthuridae')
        self.assertEqual(result, exp_result)

## Exhibit table tests
    def test_get_exhibit(self):
        self.reset_database()
        exp_result = set([
            'aegolius acadicus',
            'buteo jamaicensis',
            'buteo lagopus',
            'canis lupus',
            'canis lupus familiaris',
            'cathartes aura',
            'falco peregrinus',
            'falco sparverius',
            'haliaeetus leucocephalus',
            'ursus arctos horribilis'
        ])
        result = self.zdb.get_exhibit('Grizzly and Wolf Discovery Center')
        self.assertEqual(result, exp_result)
        
    def test_post_exhibit(self):
        self.reset_database()
        exp_result = set([
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
            'acanthurus olivaceus',
            'acanthurus pyroferus'
        ])
        add_species = set(['acanthurus olivaceus', 'acanthurus pyroferus'])
        self.zdb.post_exhibit('Grizzly and Wolf Discovery Center', exp_result)
        result = self.zdb.get_exhibit('Grizzly and Wolf Discovery Center')
        self.assertEqual(result, exp_result)

    def test_delete_exhibit(self):
        self.reset_database()
        exp_result = set([
            'aegolius acadicus',
            'buteo jamaicensis',
            'buteo lagopus',
            'canis lupus',
            'canis lupus familiaris',
            'cathartes aura',
            'falco peregrinus',
            'falco sparverius',
            'haliaeetus leucocephalus'
        ])
        self.zdb.delete_exhibit('Grizzly and Wolf Discovery Center', 'ursus arctos horribilis')
        result = self.zdb.get_exhibit('Grizzly and Wolf Discovery Center')
        self.assertEqual(result, exp_result)

## Habitat table tests
    def test_get_habitat(self):
        self.reset_database()
        exp_result = 'near the seabed at the bottom of a body of water'
        result = self.zdb.get_habitat('benthic')
        self.assertEqual(result, exp_result)

    def test_post_habitat(self):
        self.reset_database()
        exp_result = 'description'
        self.zdb.post_habitat('habitat', 'description')
        result = self.zdb.get_habitat('habitat')
        self.assertEqual(result, exp_result)

## Region table tests
    def test_get_region(self):
        self.reset_database()
        exp_result = 'north america'
        result = self.zdb.get_region('nearctic')
        self.assertEqual(result, exp_result)

    def test_post_region(self):
        self.reset_database()
        exp_result = 'description'
        self.zdb.post_region('region', 'description')
        result = self.zdb.get_region('region')
        self.assertEqual(result, exp_result)

## Species table tests
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
        self.assertEqual(result, exp_result)

    def test_put_species(self):
        self.reset_database()
        # Add a new species
        common_names = set(['Dire wolf'])
        regions = set(['holarctic'])
        habitats = set(['tundra'])
        info = {
            'Common Name': common_names,
            'Genus': 'canis',
            'Family': 'canidae',
            'Region': regions,
            'Habitat': habitats,
            'Status': 'EX'
        }
        self.zdb.post_species('canis dirus', info)
        # Update the species
        exp_result = info
        exp_result['Status'] = 'EW'
        self.zdb.put_species('canis dirus', 'Status', 'EW')
        result = self.zdb.get_species('canis dirus')
        self.assertEqual(result, exp_result)

    def test_post_species(self):
        self.reset_database()
        common_names = set(['Dire wolf'])
        regions = set(['holarctic'])
        habitats = set(['tundra'])
        exp_result = {
            'Common Name': common_names,
            'Genus': 'canis',
            'Family': 'canidae',
            'Region': regions,
            'Habitat': habitats,
            'Status': 'EX'
        }
        self.zdb.post_species('canis dirus', exp_result)
        result = self.zdb.get_species('canis dirus')
        self.assertEqual(result, exp_result)

## State table tests
    def test_get_state(self):
        self.reset_database()
        exp_result = 'North Carolina'
        result = self.zdb.get_state('NC')
        self.assertEqual(result, exp_result)

## Status table tests
    def test_get_status(self):
        self.reset_database()
        exp_result = 'data deficient'
        result = self.zdb.get_status('DD')
        self.assertEqual(result, exp_result)

## Zoo table tests
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
        result = self.zdb.get_zoo('Abilene Zoo')
        self.assertEqual(result, exp_result) 

    def test_put_zoo(self):
        self.reset_database()
        exp_result = {
            'City': 'Abilene',
            'State': 'TX',
            'Address': '2070 Zoo Lane',
            'Number of Animals': 1100,
            'Acres': 13,
            'Opening Time': '9:00',
            'Closing Time': '17:00',
            'Annual Visitors': 200000,
            'Website URL': 'http://abilenezoo.org/'
        }        
        self.zdb.put_zoo('Abilene Zoo', 'Annual Visitors', 200000)
        result = self.zdb.get_zoo('Abilene Zoo')
        self.assertEqual(result, exp_result)

    def test_post_zoo(self):
        self.reset_database()
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
        self.zdb.post_zoo('Test Zoo', exp_result)
        result = self.zdb.get_zoo('Test Zoo')
        self.assertEqual(result, exp_result)  

if __name__ == "__main__":
    unittest.main()
