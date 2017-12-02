// Get a list of species
function getSpecies() {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
      response = JSON.parse(xmlHttp.response);
      createLinks(response);
    }
  }
  xmlHttp.open("GET", "http://student04.cse.nd.edu:51042/species/", true);
  xmlHttp.send(null);
}

// Add links to the page
function createLinks(data) {
  links = '<ul>';
  for (var i in data.species) {
    species_name = data.species[i].replace('_', ' ');
    links += '<li><a href="species.html?species=' + data.species[i] + '">' + species_name + '</a></li>'
  }
  links += '</ul>'
  html = $.parseHTML(links);
  $('#species').append(html);
}

$(document).ready(function() {
  getSpecies();
});
