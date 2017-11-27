# Constants
BASEURL = '../db/'
CLASSIFICATION = 'classification.csv'
EXHIBIT = 'exhibit.csv'
HABITAT = 'habitat.csv'
REGION = 'region.csv'
SPECIES = 'species.csv'
STATE = 'state.csv'
STATUS = 'status.csv'
ZOO = 'zoo.csv'


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

    # Recreate all dict objects
    def reset_all(self):
        self.classification = dict()
        self.exhibit = dict()
        self.habitat = dict()
        self.region = dict()
        self.species = dict()
        self.state = dict()
        self.status = dict()
        self.zoo = dict()

    # Call all load functions
    def load_all(self):
        self.load_classification()
        self.load_exhibit()
        self.load_habitat()
        self.load_region()
        self.load_species()
        self.load_state()
        self.load_status()
        self.load_zoo()

## Classification table
    # Load from classification.csv
    def load_classification(self):
        with open(BASEURL+CLASSIFICATION) as cf:
            for line in cf:
                family, order, _class, phylum, kingdom, desc = line.rstrip().split(',', 6)
                desc = set(desc.split(';'))
                self.classification[family] = {
                    'Order': order,
                    'Class': _class,
                    'Phylum': phylum,
                    'Kingdom': kingdom,
                    'Desc': desc
                }

    # Get the full classification of a family
    def get_classication(self, family):
        if family not in self.classification:
            raise ValueError('%s is not an existing family' % family)
        return self.classification[family]

## Exhibit table
    # Load from exhibit.csv
    def load_exhibit(self):
        with open(BASEURL+EXHIBIT) as ef:
            for line in ef:
                zoo, species = line.rstrip().split(',', 2)
                if zoo not in self.exhibit:
                    self.exhibit[zoo] = set()
                self.exhibit[zoo].add(species)

    # Get all animals exhibited at a zoo
    def get_exhibit(self, zoo):
        if zoo in self.exhibit:
            return self.exhibit[zoo]
        else:
            return None

    # Add animal(s) to a zoo exhibit as a set
    def post_exhibit(self, zoo, species):
        # Only add to exhibit if zoo and all species exist
        if zoo not in self.zoo:
            raise ValueError('"%s" is not an existing zoo' % zoo)
        for _species in species:
            if _species not in self.species:
                raise ValueError('"%s" is not an existing species' % _species)
        # Add the species to the zoo exhibit
        if zoo not in self.exhibit:
            self.exhibit[zoo] = set()
        else:
            self.exhibit[zoo].update(species)

    # Remove an animal from a zoo exhibit
    def delete_exhibit(self, zoo, species):
        if zoo in self.exhibit and species in self.exhibit[zoo]:
            self.exhibit[zoo].remove(species)

## Habitat table
    # Load from habitat.csv
    def load_habitat(self):
        with open(BASEURL+HABITAT) as hf:
            for line in hf:
                habitat, desc = line.rstrip().split(',', 2)
                self.habitat[habitat] = desc

    # Return the habitat description
    def get_habitat(self, habitat):
        if habitat not in self.habitat:
            raise ValueError('%s is not an existing habitat' % habitat)
        return self.habitat[habitat]

    # Update the description
    def post_habitat(self, habitat, desc):
        self.habitat[habitat] = desc

## Region table
    # Load from region.csv
    def load_region(self):
        with open(BASEURL+REGION) as rf:
            for line in rf:
                region, desc = line.rstrip().split(',', 2)
                self.region[region] = desc

    # Return the region description
    def get_region(self, region):
        if region not in self.region:
            raise ValueError('%s is not an existing region' % region)
        return self.region[region]

    # Update the description
    def post_region(self, region, desc):
        self.region[region] = desc

## Species table
    # Load from species.csv
    def load_species(self):
        with open(BASEURL+SPECIES) as spf:
            for line in spf:
                species, common_name, genus, family, region, habitat, status = line.rstrip().split(',', 7)
                common_names = set(common_name.split(';'))
                habitats = set(habitat.split(';'))

                self.species[species] = {
                    'Common Name': common_names,
                    'Genus': genus,
                    'Family': family,
                    'Region': region,
                    'Habitat': habitats,
                    'Status': status
                }

    # Get the species information from the species name
    def get_species(self, species):
        if species not in self.species:
            raise ValueError('%s is not an existing species' % species)
        return self.species[species]

    # Update a column in the species table
    def put_species(self, species, column, info):
        if species not in self.species:
            raise ValueError('"%s" is not an existing species' % species)
        # If the column is a set, pass in a set as info and update existing set
        if type(self.species[species][column]) is set:
            self.species[species][column].update(info)
        # Otherwise pass in a string and replace current string
        else:
            self.species[species][column] = info

    # Add a new species
    def post_species(self, new_species, info):
        # Foreign key constraints
        if info['Family'] not in self.classification:
            raise ValueError('"%s" is not an existing family name' % info['Family'])
        for region in info['Region']:
            if region not in self.region:
                raise ValueError('"%s" is not an existing region' % region)
        for habitat in info['Habitat']:
            if habitat not in self.habitat:
                raise ValueError('"%s" is not an existing habitat' % habitat)
        self.species[new_species] = info

## State table
    # Load from state.csv
    def load_state(self):
        with open(BASEURL+STATE) as sf:
            for line in sf:
                abbrev, state = line.rstrip().split(',', 2)
                self.state[abbrev] = state

    # Get the full state name
    def get_state(self, abbrev):
        if abbrev not in self.state:
            raise ValueError('%s is not an existing state abbreviation' % abbrev)
        return self.state[abbrev]

## Status table
    # Load from status.csv
    def load_status(self):
        with open(BASEURL+STATUS) as stsf:
            for line in stsf:
                level, status, description = line.rstrip().split(',')
                self.status[status] = {
                    'Level': int(level),
                    'Description': description
                }

    # Get a list of the statuses in order
    def get_statuses(self):
        statuses = []
        for i in range(8):
            for status, info in self.status.items():
                if info['Level'] == i:
                    statuses.append(status)
        return statuses

    # Get the status description
    def get_status(self, status):
        if status not in self.status:
            raise ValueError('%s is not an existing status' % status)
        return self.status[status]['Description']

## Zoo table
    # Load from zoo.csv
    def load_zoo(self):
        with open(BASEURL+ZOO) as zf:
            for line in zf:
                zoo, city, state, address, num_animals, acres, opening_time, closing_time, annual_visitors, website_url = line.rstrip().split(',', 10)
                self.zoo[zoo] = {
                    'City': city,
                    'State': state,
                    'Address': address,
                    'Number of Animals': int(num_animals),
                    'Acres': int(acres),
                    'Opening Time': opening_time,
                    'Closing Time': closing_time,
                    'Annual Visitors': int(annual_visitors),
                    'Website URL': website_url
                }

    def get_zoo(self, zoo):
        if zoo not in self.zoo:
            raise ValueError('%s is not an existing zoo' % zoo)
        return self.zoo[zoo]

    # Update a column in the zoo table
    def put_zoo(self, zoo, column, info):
        if zoo not in self.zoo:
            raise ValueError('%s is not an existing zoo' % zoo)
        self.zoo[zoo][column] = info

    # Add a new zoo
    def post_zoo(self, new_zoo, info):
        if info['State'] not in self.state:
            raise ValueError('%s is not an existing state' % info['State'])
        self.zoo[new_zoo] = info
