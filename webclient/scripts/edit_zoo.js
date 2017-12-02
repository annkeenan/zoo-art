// Get zoo
function getZoo(zoo) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
      zoo = JSON.parse(xmlHttp.response);
      states = getStates();
      createForm(zoo, states);
    }
  }
  xmlHttp.open("GET", "http://student04.cse.nd.edu:51042/zoo/" + zoo, true);
  xmlHttp.send(null);
}

function getStates() {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
      response = JSON.parse(xmlHttp.response);
      return response;
    }
  }
  xmlHttp.open("GET", "http://student04.cse.nd.edu:51042/state/", true);
  xmlHttp.send(null);
}

// Add links to the page
function createDropdowns(states) {
  // Hour
  hours = '';
  for (var i = 0; i < 24; i++) {
    hours += '<option value="' + i + '">'+ i + '</option>'
  }
  $('#id_open_hour').append($.parseHTML(hours));
  $('#id_close_hour').append($.parseHTML(hours));
  // Minutes
  minutes = ['00', '15', '30', '45'];
  for (var m in minutes) {
    console.log(m);
  }
  // States
  console.log(states);
}

function createForm(zoo, states) {
  createDropdowns(states);
}

$(document).ready(function() {
  let params = (new URL(document.location)).searchParams;
  let zoo = params.get("zoo");
  getZoo(zoo);
});
