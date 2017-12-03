class _zoo_database:
    def __init__(self):
        self.BASEURL = '../db/'
        self.reset_all()
        self.load_all()

    # Recreate all dict objects
    def reset_all(self):
        self.classification = dict()
        self.exhibit_species = dict()
        self.exhibit_zoo = dict()
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
        with open(self.BASEURL+'classification.csv') as cf:
            for line in cf:
                family, order, _class, phylum, kingdom, desc = line.rstrip().split(',', 6)
                desc = set(desc.split(';'))
                self.classification[family] = {
                    'order': order,
                    'class': _class,
                    'phylum': phylum,
                    'kingdom': kingdom,
                    'desc': desc
                }

    # Get a list of all families in alphabetical order
    def get_families(self):
        return sorted(self.classification.keys())

    # Get the full classification of a family
    def get_classication(self, family):
        if family not in self.classification:
            raise ValueError('%s is not an existing family' % family)
        return self.classification[family]

    def post_classification(self, family, info):
        info['desc'] = set(info['desc'])
        self.classification[family] = info

## Exhibit table
    # Load from exhibit.csv
    def load_exhibit(self):
        with open(self.BASEURL+'exhibit.csv') as ef:
            for line in ef:
                zoo, species = line.rstrip().split(',', 2)
                species = species.replace(' ', '_')
                zoo = ''.join(i for i in zoo.replace(' ', '_') if (i.isalpha() or i == '_'))

                if zoo not in self.exhibit_zoo:
                    self.exhibit_zoo[zoo] = set()
                self.exhibit_zoo[zoo].add(species)

                if species not in self.exhibit_species:
                    self.exhibit_species[species] = set()
                self.exhibit_species[species].add(zoo)

    # Get all animals exhibited at a zoo in alphabetical order
    def get_exhibited_zoo(self, zoo):
        if zoo in self.exhibit_zoo:
            return sorted(self.exhibit_zoo[zoo])
        else:
            return None

    # Get the species that are not at a zoo
    def get_not_exhibited_zoo(self, zoo):
        exhibited_species = self.get_exhibited_zoo(zoo)
        if zoo in self.exhibit_zoo:
            not_exhibited = []
            for _species in self.species:
                if _species not in exhibited_species:
                    not_exhibited.append(_species)
            return not_exhibited
        else:
            return None

	# Get all the zoos that a species are in
    def get_exhibits_species(self, species):
        if species in self.exhibit_species:
            return sorted(self.exhibit_species[species])
        else:
            return None

    # Add animal(s) to a zoo exhibit as a set
	# Add zoo(s) to a animal's zoos
    def post_exhibit(self, zoo, species):
        # Only add to exhibit if zoo and all species exist
        if zoo not in self.zoo:
            raise ValueError('"%s" is not an existing zoo' % zoo)
        for _species in species:
            if _species not in self.species:
                raise ValueError('"%s" is not an existing species' % _species)
        # Add the species to the zoo exhibit
        if zoo not in self.exhibit_zoo:
            self.exhibit_zoo[zoo] = set()
        else:
            self.exhibit_zoo[zoo].update(species)

        # Add the zoo to the species
        for _species in species:
            if _species not in self.exhibit_species:
                self.exhibit_species[_species] = set()
            else:
                self.exhibit_species[_species].update(zoo)

    # Remove an animal from a zoo exhibit and remove that zoo from that animal
    def delete_exhibit(self, zoo, species):
        if zoo in self.exhibit_zoo and species in self.exhibit_zoo[zoo]:
            self.exhibit_zoo[zoo].remove(species)
        if species in self.exhibit_species and zoo in self.exhibit_species[species]:
            self.exhibit_species[species].remove(zoo)

## Habitat table
    # Load from habitat.csv
    def load_habitat(self):
        with open(self.BASEURL+'habitat.csv') as hf:
            for line in hf:
                habitat, desc = line.rstrip().split(',', 2)
                self.habitat[habitat] = desc

    # Get a list of all habitats in alphabetical order
    def get_habitats(self):
        return sorted(self.habitat.keys())

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
        with open(self.BASEURL+'region.csv') as rf:
            for line in rf:
                region, desc = line.rstrip().split(',', 2)
                self.region[region] = desc

    # Get a list of all regions in alphabetical order
    def get_regions(self):
        return sorted(self.region.keys())

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
        with open(self.BASEURL+'species.csv') as spf:
            for line in spf:
                species, common_name, genus, family, region, habitat, status = line.rstrip().split(',', 7)
                species = species.replace(' ', '_')
                common_names = set(common_name.split(';'))
                regions = set(region.split(';'))
                habitats = set(habitat.split(';'))
                self.species[species] = {
                    'common_name': common_names,
                    'genus': genus,
                    'family': family,
                    'region': regions,
                    'habitat': habitats,
                    'status': status}

    # Get a list of all species in alphabetical order
    def get_all_species(self):
        return sorted(self.species.keys())

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
            self.species[species][column] = set(info)
        # Otherwise pass in a string and replace current string
        else:
            self.species[species][column] = info

    # Add a new species
    def post_species(self, new_species, info):
        # Foreign key constraints
        if info['family'] not in self.classification:
            raise ValueError('"%s" is not an existing family name' % info['family'])
        for region in info['region']:
            if region not in self.region:
                raise ValueError('"%s" is not an existing region' % region)
        for habitat in info['habitat']:
            if habitat not in self.habitat:
                raise ValueError('"%s" is not an existing habitat' % habitat)
        # Convert lists to sets
        info['common_name'] = set(info['common_name'])
        info['region'] = set(info['region'])
        info['habitat'] = set(info['habitat'])
        self.species[new_species] = info

## State table
    # Load from state.csv
    def load_state(self):
        with open(self.BASEURL+'state.csv') as sf:
            for line in sf:
                abbrev, state = line.rstrip().split(',', 2)
                self.state[abbrev] = state

    # Get a list of all states in alphabetical order
    def get_states(self):
        return sorted(self.state.keys())

    # Get the full state name
    def get_state(self, abbrev):
        if abbrev not in self.state:
            raise ValueError('%s is not an existing state abbreviation' % abbrev)
        return self.state[abbrev]

## Status table
    # Load from status.csv
    def load_status(self):
        with open(self.BASEURL+'status.csv') as stsf:
            for line in stsf:
                level, status, description = line.rstrip().split(',')
                self.status[status] = {
                    'level': int(level),
                    'description': description}

    # Get a list of the statuses in order
    def get_statuses(self):
        statuses = []
        for i in range(8):
            for status, info in self.status.items():
                if info['level'] == i:
                    statuses.append(status)
        return statuses

    # Get the status description
    def get_status(self, status):
        if status not in self.status:
            raise ValueError('%s is not an existing status' % status)
        return self.status[status]['description']

## Zoo table
    # Load from zoo.csv
    def load_zoo(self):
        with open(self.BASEURL+'zoo.csv') as zf:
            for line in zf:
                zoo, city, state, address, num_animals, acres, opening_time, closing_time, annual_visitors, website_url = line.rstrip().split(',', 10)
                zoo = ''.join(i for i in zoo.replace(' ', '_') if (i.isalpha() or i=='_'))
                self.zoo[zoo] = {
                    'city': city,
                    'state': state,
                    'address': address,
                    'num_animals': int(num_animals),
                    'acres': int(acres),
                    'opening_time': opening_time,
                    'closing_time': closing_time,
                    'annual_visitors': int(annual_visitors),
                    'website_url': website_url}

    # Get a list of all zoos in alphabetical order
    def get_zoos(self):
        return sorted(self.zoo.keys())

    # Get information about a zoo
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
        if info['state'] not in self.state:
            raise ValueError('%s is not an existing state' % info['state'])
        self.zoo[new_zoo] = info
