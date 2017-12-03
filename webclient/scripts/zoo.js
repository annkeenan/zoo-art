// Get info on a Zoo
function getZoo() {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
      response = JSON.parse(xmlHttp.response);
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
  links = '<ul>';
  for (var i in data.species) {
    species_name = data.species[i].replace('_', ' ');
    links += '<li><a href="species.html?species=' + data.species[i] + '">' + species_name + '</a></li>'
  }
  links += '</ul>';
  html = $.parseHTML(links);
  $('#species').append(html);
}


$(document).ready(function() {
  getZoo();
  getExhibitZoo();
});
