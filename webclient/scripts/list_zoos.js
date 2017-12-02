// Get a list of zoos
function getZoos() {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
      response = JSON.parse(xmlHttp.response);
      createLinks(response);
    }
  }
  xmlHttp.open("GET", "http://student04.cse.nd.edu:51042/zoo/", true);
  xmlHttp.send(null);
}

// Add links to the page
function createLinks(data) {
  links = '<ul>';
  for (var z in data.zoos) {
    zoo_name = z.replace('_', ' ');
    links += '<li><a href="/zoo.html?zoo=' + z + '">' + zoo_name + '</a></li>'
  }
  links += '</ul>'
  html = $.parseHTML(links);
  $('#zoos').append(html);
}

$(document).ready(function() {
  getZoos();
});
