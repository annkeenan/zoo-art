
## List zoos

/list_zoos.html

GET /zoo/

Display the list of zoos as links to zoo.html?zoo=[zoo]

## Zoo

/zoo.html?zoo=[zoo]

GET /zoo/[:zoo]
GET /exhibit/[:zoo]/[True]
GET /exhibit/[:zoo]/[False]

Display the information about the zoo and list of species exhibited at that zoo.
Modal view for adding exhibits that displays a dropdown of species not currently
exhibited. Allows for removing exhibits with delete buttons next to the species.

## Edit zoo

/edit_zoo.html?zoo=[zoo]

GET /zoo/[:zoo]
GET /state/

PUT /zoo/[:zoo]

Display any preexisting information about the zoo in editable fields.

## Add zoo

/add_zoo.html

GET /state/

POST /zoo/

Display a blank form with editable fields.

## List species

/list_species.html

GET /species/

Display the list of species as links to species.html?species=[species]

## Species

/species.html?species=[species]

GET /species/[:species]
GET /classification/[:family]
GET /exhibit/[:species]

Display information about the species and list of zoos exhibiting that species.

## Edit species

/edit_species.html?species=[species]

GET /species/[:species]
GET /classification/
GET /region/
GET /habitat/
GET /status/

PUT /species/[:species]

Display any preexisting information about the species in editable fields.

## Add species

/add_species.html

GET /classification/
GET /region/
GET /habitat/
GET /status/

POST /species/

Display a blank form with editable fields.
