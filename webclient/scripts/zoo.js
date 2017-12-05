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
  xmlHttp.open("GET", "http://student04.cse.nd.edu:51056/zoo/" + zooString, true);
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
  xmlHttp.open("GET", "http://student04.cse.nd.edu:51056/exhibit/" + zooString + "/true", true);
  xmlHttp.send(null);
}

function deleteSpecies(args) {
  alert('update display' + args);
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
  $('#species').append(html);
}


$(document).ready(function() {
  getZoo();
  getExhibitZoo();
});
