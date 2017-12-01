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
