from constants import *

class _zoo_database:
    def __init__(self):
        self.classification = dict()
        self.exhibit = dict()
        self.habitat = dict()
        self.region = dict()
        self.species = dict()
        self.state = dict()
        self.status = dict()
        self.zoo = dict()

    def reset_all(self):
        self.classification = dict()
        self.exhibit = dict()
        self.habitat = dict()
        self.region = dict()
        self.species = dict()
        self.state = dict()
        self.status = dict()
        self.zoo = dict()

    # Classification table
    def load_classification(self):
        with open(BASEURL+CLASSIFICATION) as cf:
            for line in cf:
                _family, _order, _class, _phylum, _kingdom, _desc = line.rstrip().split(',', 6)
                _desc = set(_desc.split(';'))
                self.classification[_family] = {
                    'Order': _order,
                    'Class': _class,
                    'Phylum': _phylum,
                    'Kingdom': _kingdom,
                    'Desc': _desc
                }

    def get_classication(self, family):
        return self.classification[family]

    # Habitat table
    def load_habitat(self):
        with open(BASEURL+HABITAT) as hf:
            for line in hf:
                _habitat, _desc = line.rstrip().split(',', 2)
                self.habitat[_habitat] = _desc

    def get_habitat(self, habitat):
        return self.habitat[habitat]

    # Region table
    def load_region(self):
        with open(BASEURL+REGION) as rf:
            for line in rf:
                _region, _desc = line.rstrip().split(',', 2)
                self.region[_region] = _desc

    def get_region(self, region):
        return self.region[region]
