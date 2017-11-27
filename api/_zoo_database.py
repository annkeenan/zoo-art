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
    
    # State table 
    def load_state(self):
        with open(BASEURL+STATE) as sf:
            for line in sf:
                abbrev, state = line.rstrip().split(',')
                self.state[abbrev] = state

    def get_state(self, abbrev):
        return self.state[abbrev]

    # Species Table
    def load_species(self):
        with open(BASEURL+SPECIES) as spf:
            for line in spf:
                species, common_name, genus, family, region, habitat, status = line.rstrip().split(',')
                common_names = set()
                habitats = set()

                for name in common_name.split(';'):
                    common_names.add(name)
                for hab in habitat.split(';'):
                    habitats.add(hab)

                self.species[species] = {
                    'Common Name': common_names,
                    'Genus': genus,
                    'Family': family,
                    'Region': region,
                    'Habitat': habitats,
                    'Status': status
                }

    def get_species(self, species):
        return self.species[species]

    # Exhibit Table 
    def load_exhibit(self):
        with open(BASEURL+EXHIBIT) as ef:
            for line in ef:
                zoo, species = line.rstrip().split(',')
                if zoo not in self.exhibit:
                    self.exhibit[zoo] = set([species])
                else:
                    self.exhibit[zoo].add(species)

    def get_exhibit(self, exhibit):
        return self.exhibit[exhibit]
    
    #Zoo Table
    def load_zoo(self):
	with open(BASEURL+ZOO) as zf:
            for line in zf:
                zoo, city, state, address, num_animals, acres, opening_time, closing_time, annual_visitors, website_url = line.rstrip().split(',')
                self.zoo[zoo] = {
                    'City': city,
                    'State': state,
                    'Address': address,
                    'Number of Animals': num_animals,
                    'Acres': acres,
                    'Opening Time': opening_time,
                    'Closing Time': closing_time,
                    'Annual Visitors': annual_visitors,
                    'Website URL': website_url
                }
                
    def get_zoo(self, zoo):
        return self.zoo[zoo]

    #Status Table
    def load_status(self):
        with open(BASEURL+STATUS) as stsf:
            for line in stsf:
                level, status, description = line.rstrip().split(',')
                self.status[status] = {
                    'Level': level,
                    'Description': description
                }
           
    def get_status(self, status):
        return self.status[status]
