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
        response = JSON.parse(xmlHttp.response);
        if (response.result == 'success') {
          zoo_info = response.zoo;
        } else {
          zoo_info = {}
        }
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
        response = JSON.parse(xmlHttp.response);
        if (response.result == 'success') {
          state_info = response.states;
        } else {
          state_info = {}
        }
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
    for (var i in state_info) {
      state_options += '<option value="' + state_info[i] + '">'+ state_info[i] + '</option>'
    }
    $('#id_state').append($.parseHTML(state_options));

  }

  function createForm() {
    createDropdowns();
    $('#id_zoo_name').val(zoo.split('_').join(' '));
    $('#id_zoo_website').val(zoo_info.'website url');
  }

  function processForm() {
    console.log('processing');
  }
}

$(document).ready(function() {
  let params = (new URL(document.location)).searchParams;
  let zoo = params.get("zoo");
  edit_zoo(zoo);
});
