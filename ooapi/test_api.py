from _zoo_database import _zoo_database
import unittest


class TestZooDatabase(unittest.TestCase):
    zdb = _zoo_database()

    def reset_database(self):
        self.zdb.reset_all()
        self.zdb.load_all()

## Classification table tests
    def test_get_families(self):
        self.reset_database()
        result = self.zdb.get_families()
        self.assertIsInstance(result, list)

    def test_get_classification(self):
        self.reset_database()
        exp_result = {
            'order': 'perciformes',
            'class': 'actinopterygii',
            'phylum': 'chordata',
            'kingdom': 'animalia',
            'desc': {'surgeonfish', 'tang', 'unicornfish'}
        }
        result = self.zdb.get_classication('acanthuridae')
        self.assertEqual(result, exp_result)

    def test_post_classification(self):
        self.reset_database()
        exp_result = {
            'order': 'perciformes',
            'class': 'actinopterygii',
            'phylum': 'chordata',
            'kingdom': 'animalia',
            'desc': {'surgeonfish', 'tang', 'unicornfish'}
        }
        self.zdb.post_classification('test', exp_result)
        result = self.zdb.get_classication('test')
        self.assertEqual(result, exp_result)

## Exhibit table tests
    def test_get_exhibits_zoo(self):
        self.reset_database()
        exp_result = [
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
        ]

        result = self.zdb.get_exhibited_zoo('Grizzly_and_Wolf_Discovery_Center')
        self.assertEqual(result, exp_result)

    def test_get_not_exhibits_zoo(self):
        self.reset_database()
        result = self.zdb.get_not_exhibited_zoo('Grizzly_and_Wolf_Discovery_Center')
        self.assertIsInstance(result, list)

    def test_get_exhibits_species(self):
        self.reset_database()
        exp_result = [
     		'Baton_Rouge_Zoo',
			'Bronx_Zoo',
			'Brookfield_Zoo',
			'Chahinkapa_Zoo',
			'Connecticuts_Beardsley_Zoo',
			'Fossil_Rim_Wildlife_Center',
			'Great_Plains_Zoo',
			'Minnesota_Zoo',
			'North_Carolina_Zoo',
			'Potawatomi_Zoo'
        ]
        result = self.zdb.get_exhibits_species('bison_bison')
        self.assertEqual(result, exp_result)


    def test_post_exhibit(self):
        self.reset_database()
        exp_result = [
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
        ]
        add_species = ['acanthurus_olivaceus', 'acanthurus_pyroferus']
        self.zdb.post_exhibit('Grizzly_and_Wolf_Discovery_Center', add_species)
        result = self.zdb.get_exhibited_zoo('Grizzly_and_Wolf_Discovery_Center')
        self.assertEqual(result, exp_result)

    def test_delete_exhibit(self):
        self.reset_database()
        exp_result = [
            'aegolius_acadicus',
            'buteo_jamaicensis',
            'buteo_lagopus',
            'canis_lupus',
            'canis_lupus_familiaris',
            'cathartes_aura',
            'falco_peregrinus',
            'falco_sparverius',
            'haliaeetus_leucocephalus',
        ]
        self.zdb.delete_exhibit('Grizzly_and_Wolf_Discovery_Center', 'ursus_arctos_horribilis')
        result = self.zdb.get_exhibited_zoo('Grizzly_and_Wolf_Discovery_Center')
        self.assertEqual(result, exp_result)

## Habitat table tests
    def test_get_habitats(self):
        self.reset_database()
        result = self.zdb.get_habitats()
        self.assertIsInstance(result, list)

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
    def test_get_regions(self):
        self.reset_database()
        result = self.zdb.get_regions()
        self.assertIsInstance(result, list)

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
    def test_get_all_species(self):
        self.reset_database()
        result = self.zdb.get_all_species()
        self.assertIsInstance(result, list)

    def test_get_species(self):
        self.reset_database()
        common_names = set(['Blue-Throated Macaw', 'Caninde Macaw', 'Wagler\'s Macaw'])
        regions = set(['neotropical'])
        habitats = set(['savanna/grassland', 'forest'])
        exp_result = {
            'common_name': common_names,
            'genus': 'ara',
            'family': 'psittacidae',
            'region': regions,
            'habitat': habitats,
            'status': 'CR'
        }
        result = self.zdb.get_species('ara_glaucogularis')
        self.assertEqual(result, exp_result)

    def test_put_species(self):
        self.reset_database()
        # Add a new species
        common_names = set(['Dire wolf'])
        regions = set(['holarctic'])
        habitats = set(['tundra'])
        info = {
            'common_name': common_names,
            'genus': 'canis',
            'family': 'canidae',
            'region': regions,
            'habitat': habitats,
            'status': 'EX'
        }
        self.zdb.post_species('canis_dirus', info)
        # Update the species
        exp_result = info
        exp_result['Status'] = 'EW'
        self.zdb.put_species('canis_dirus', 'Status', 'EW')
        result = self.zdb.get_species('canis_dirus')
        self.assertEqual(result, exp_result)

    def test_post_species(self):
        self.reset_database()
        common_names = set(['Dire wolf'])
        regions = set(['holarctic'])
        habitats = set(['tundra'])
        exp_result = {
            'common_name': common_names,
            'genus': 'canis',
            'family': 'canidae',
            'region': regions,
            'habitat': habitats,
            'status': 'EX'
        }
        self.zdb.post_species('canis_dirus', exp_result)
        result = self.zdb.get_species('canis_dirus')
        self.assertEqual(result, exp_result)

## State table tests
    def test_get_states(self):
        self.reset_database()
        result = self.zdb.get_states()
        self.assertIsInstance(result, list)

    def test_get_state(self):
        self.reset_database()
        exp_result = 'North Carolina'
        result = self.zdb.get_state('NC')
        self.assertEqual(result, exp_result)

## Status table tests
    def test_get_statuses(self):
        self.reset_database()
        result = self.zdb.get_statuses()
        self.assertIsInstance(result, list)

    def test_get_status(self):
        self.reset_database()
        exp_result = 'data deficient'
        result = self.zdb.get_status('DD')
        self.assertEqual(result, exp_result)

## Zoo table tests
    def test_get_zoos(self):
        self.reset_database()
        result = self.zdb.get_zoos()
        self.assertIsInstance(result, list)

    def test_get_zoo(self):
        self.reset_database()
        exp_result = {
            'city': 'Abilene',
            'state': 'TX',
            'address': '2070 Zoo Lane',
            'num_animals': 1100,
            'acres': 13,
            'opening_time': '9:00',
            'closing_time': '17:00',
            'annual_visitors': 175000,
            'website_url': 'http://abilenezoo.org/'
        }
        result = self.zdb.get_zoo('Abilene_Zoo')
        self.assertEqual(result, exp_result)

    def test_put_zoo(self):
        self.reset_database()
        exp_result = {
            'city': 'Abilene',
            'state': 'TX',
            'address': '2070 Zoo Lane',
            'num_animals': 1100,
            'acres': 13,
            'opening_time': '9:00',
            'closing_time': '17:00',
            'annual_visitors': 200000,
            'website_url': 'http://abilenezoo.org/'
        }
        self.zdb.put_zoo('Abilene_Zoo', 'annual_visitors', 200000)
        result = self.zdb.get_zoo('Abilene_Zoo')
        self.assertEqual(result, exp_result)

    def test_post_zoo(self):
        self.reset_database()
        exp_result = {
            'city': 'Yorba Linda',
            'state': 'CA',
            'address': '1234 Zoo Lane',
            'num_animals': 777,
            'acres': 19,
            'opening_time': '9:00',
            'closing_time': '17:00',
            'annual_visitors': 45000,
            'website_url': 'http://zoo.org/'
        }
        self.zdb.post_zoo('Test_Zoo', exp_result)
        result = self.zdb.get_zoo('Test_Zoo')
        self.assertEqual(result, exp_result)


if __name__ == "__main__":
    unittest.main()
