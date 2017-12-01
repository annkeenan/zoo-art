# Webservice

## Use

The webservice runs on port 51042.

The classification, region, habitat, state, and status tables are used as
reference for when a species is to be added, as the columns in the species
table reference the key in these tables of the database. The lists will be
queried through a GET request that fetches a list of all stored elements in the
specified table at the url /classification/, /habitat/, /region/, /state/, or
/status/. Users may also add to these tables with a post request, or get an
individual entry in the table by querying on a specific entry id.

The exhibit table holds the zoo names and the species in those exhibits.
When posting an exhbit the user can add a species to a zoo. A get request to 
an exhibit returns a list of all the species in that exhibit, and a delte 
removes a species from an exhibit.

The species table holds the species and its Common Names, Genus, Family, Region,
Habitat, and Status. Using a get requests a user can get all of the species or
you can get a single species. You can modify a species' specifications with a put request.
If a new species is discorved then you can post a new species.

The zoo table holds a list of the zoo names. A get request to /zoo/ will
return a list of all zoo names. A get request to /zoo/:zoo_name will 
return the columns of the Zoo table for that specific zoo as a dict. The info dict
will contain the stored elements of city, state, address, number of animals, 
acres, opening time, closing time, annual visitors, and website url. Users may 
use a post request to add a zoo or a put request to change a specific columns 
info for a zoo. 
