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
        self.zdb.load_species()
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
        self.zdb.load_species()
        self.zdb.post_species(post_dict)
        result = self.zdb.get_species('Dire wolf')
        self.assertEquals(result, exp_result)

    def test_post_exhibit(self):
        self.reset_database()
        post_dict = {
            'zoo name': 'Blah Zoo',
            'species': set(['Kangaroo', 'Zebra'])
        }
        exp_result = set(['Kangaroo', 'Zebra']) 
        self.zdb.load_exhibit()
        self.zdb.post_exhibit(post_dict)
        result = self.zdb.get_exhibit('Blah Zoo')
        self.assertEquals(result, exp_result)

    def test_delete_exhibit(self):
        self.reset_database()
        self.zdb.load_exhibit()
        self.zdb.delete_exhibit('Birmingham Zoo')
        self.assertEquals(self.zdb.get_exhibit('Birmingham Zoo'), None)

if __name__ == "__main__":
    unittest.main()
