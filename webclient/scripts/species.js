// Get info on a Species
function getSpecies() {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
      response = JSON.parse(xmlHttp.response);
      var link = document.getElementById("editLink");
      link.setAttribute("href", "edit_species.html?species=" + speciesString);
      displaySpecies(response, speciesString);
      getClassification(response[speciesString].family);
    }
  }

  var urlParams = new URLSearchParams(window.location.search);
  var speciesString = urlParams.get('species');
  xmlHttp.open("GET", "http://student04.cse.nd.edu:51056/species/" + speciesString, true);
  xmlHttp.send(null);

}

// get classification of an animals family
function getClassification(family) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
      response = JSON.parse(xmlHttp.response);
      displayClassification(response);
    }
  }

  xmlHttp.open("GET", "http://student04.cse.nd.edu:51056/classification/" + family, true);
  xmlHttp.send(null);
}

function getExhibitSpecies() {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
      response = JSON.parse(xmlHttp.response);
      createLinks(response);
    }
  }
  var urlParams = new URLSearchParams(window.location.search);
  var speciesString = urlParams.get('species');
  xmlHttp.open("GET", "http://student04.cse.nd.edu:51056/exhibit/" + speciesString, true);
  xmlHttp.send(null);
}


// Add species info to the page
function displaySpecies(data, name) {
  var speciesName = name.split('_').join(' ');
  $('#speciesName').append(speciesName);
  speciesInfo = '';
  for (key in data[name]) {
    speciesInfo+= '<p><b>' + key + '</b>' + ' '+ data[name][key] + '</p>'
  }
  html = $.parseHTML(speciesInfo);
  $('#speciesInfo').append(html);
}

// Add species info to the page
function displayClassification(data) {
  classificationInfo = '';
  for (key in data.classification) {
    classificationInfo+= '<p><b>' + key + '</b>' + ' '+ data.classification[key] + '</p>'
  }
  html = $.parseHTML(classificationInfo);
  $('#classificationInfo').append(html);
}

// Add links to the page
function createLinks(data) {
  links = '<ul>';
  for (var i in data.zoos) {
    zoo_name = data.zoos[i].split('_').join(' ');
    links += '<li><a href="zoo.html?zoo=' + data.zoos[i] + '">' + zoo_name + '</a></li>'
  }
  links += '</ul>';
  html = $.parseHTML(links);
  $('#zoos').append(html);
}


$(document).ready(function() {
  getSpecies();
  getExhibitSpecies();
});
