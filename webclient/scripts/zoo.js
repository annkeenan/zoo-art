// Get info on a Zoo
function getZoo() {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
      response = JSON.parse(xmlHttp.response);
      var link = document.getElementById("editLink");
      link.setAttribute("href", "edit_zoo.html?zoo=" + zooString)
      displayZoo(response, zooString);
    }
  }

  var urlParams = new URLSearchParams(window.location.search);
  var zooString = urlParams.get('zoo');
  xmlHttp.open("GET", "http://student04.cse.nd.edu:51042/zoo/" + zooString, true);
  xmlHttp.send(null);
}

function getExhibitZoo() {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
      response = JSON.parse(xmlHttp.response);
      createLinks(response);
    }
  }
  var urlParams = new URLSearchParams(window.location.search);
  var zooString = urlParams.get('zoo');
  xmlHttp.open("GET", "http://student04.cse.nd.edu:51042/exhibit/" + zooString + "/true", true);
  xmlHttp.send(null);
}

function deleteSpecies(args) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
      getExhibitZoo();
    }
  }
  var urlParams = new URLSearchParams(window.location.search);
  var zooString = urlParams.get('zoo');
  xmlHttp.open("DELETE", "http://student04.cse.nd.edu:51042/exhibit/" + zooString + "/"+ args, true);
  xmlHttp.send(null);
}

function getSpeciesNotExhbited() {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
      response = JSON.parse(xmlHttp.response);
      fillDropDown(response);
    }
  }
  var urlParams = new URLSearchParams(window.location.search);
  var zooString = urlParams.get('zoo');
  xmlHttp.open("GET", "http://student04.cse.nd.edu:51042/exhibit/" + zooString + "/false", true);
  xmlHttp.send(null);
}

function addSpecies(args) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
      getExhibitZoo();
    }
  }
  alert(args);
  var dict  = JSON.stringify({
    "species": [args]
  });
  var urlParams = new URLSearchParams(window.location.search);
  var zooString = urlParams.get('zoo');
  xmlHttp.open("POST", "http://student04.cse.nd.edu:51042/exhibit/" + zooString, true);
  xmlHttp.send(dict);
}

// Add zoo info to the page
function displayZoo(data, name) {
  var zooName = name.split('_').join(' ');
  $('#zooName').append(zooName);
  zooInfo = '';
  for (key in data.zoo) {
    zooInfo+= '<p><b>' + key + '</b>' + ' '+ data.zoo[key] + '</p>'
  }
  html = $.parseHTML(zooInfo);
  $('#zooInfo').append(html);
}

// Add links to the page
function createLinks(data) {
  links = '<ul class="fa-ul">';
  for (var i in data.species) {
    species_name = data.species[i].replace('_', ' ');
    links += '<li><span onclick="deleteSpecies('+ '\'' + data.species[i] + '\'' +')"><i class="fa fa-trash" aria-hidden="true"></i></span><a href="species.html?species=' + data.species[i] + '">' + species_name + '</a></li>'
  }
  links += '</ul>';
  html = $.parseHTML(links);
  //$('#species').append(html);
  $('#species').html(html);
}

// fill dropdown with animals not in the exhibit
function fillDropDown(data) {
  dropdownitems = '';
  for (var i in data.species) {
    species_name = data.species[i].replace('_', ' ');
    dropdownitems += '<li><a onclick="addSpecies('+ '\'' + data.species[i] + '\'' +')"><i class="fa fa-plus-circle" aria-hidden="true"></i> '+ species_name +'</a></li>'
  }
  html = $.parseHTML(dropdownitems);
  //$('#species').append(html);
  $('#dropdownitems').html(html);
}


$(document).ready(function() {
  getZoo();
  getExhibitZoo();
});
