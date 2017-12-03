function edit_zoo(zoo) {
  // Store ajax response values
  var zoo_info;
  var state_info;

  // Start chain of ajax requests
  getZoo(zoo);

  // Bind the form
  $('#id_zoo_form').bind('submit', processForm);

  // Get zoo
  function getZoo(zoo) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
        zoo_info = JSON.parse(xmlHttp.response);
        getStates();
      }
    }
    xmlHttp.open("GET", "http://student04.cse.nd.edu:51042/zoo/" + zoo, true);
    xmlHttp.send(null);
  }

  // Get a list of states
  function getStates() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
        state_info = JSON.parse(xmlHttp.response);
        createForm();
      }
    }
    xmlHttp.open("GET", "http://student04.cse.nd.edu:51042/state/", true);
    xmlHttp.send(null);
  }

  // Add links to the page
  function createDropdowns() {
    // Hour
    hours = '';
    for (var i = 0; i < 24; i++) {
      hours += '<option value="' + i + '">'+ i + '</option>'
    }
    $('#id_open_hour').append($.parseHTML(hours));
    $('#id_close_hour').append($.parseHTML(hours));

    // Minutes
    minutes = '<option value="0">00</option><option value="30">30</option>';
    $('#id_open_minute').append($.parseHTML(minutes));
    $('#id_close_minute').append($.parseHTML(minutes));

    // States
    state_options = '';
    for (var i in state_info.states) {
      state_options += '<option value="' + state_info.states[i] + '">'+ state_info.states[i] + '</option>'
    }
    $('#id_state').append($.parseHTML(state_options));

  }

  function createForm() {
    createDropdowns();
  }
}

$(document).ready(function() {
  let params = (new URL(document.location)).searchParams;
  let zoo = params.get("zoo");
  edit_zoo(zoo);
});
