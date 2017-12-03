function add_zoo() {
  // Store ajax response values
  var state_info;

  // Start chain of ajax requests
  getStates();

  // Bind the form
  $('#id_zoo_form').bind('submit', processForm);

  function getStates() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
        response = JSON.parse(xmlHttp.response);
        if (response.result == 'success') {
          state_info = response.states;
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
    $('#id_opening_hour').append($.parseHTML(hours));
    $('#id_closing_hour').append($.parseHTML(hours));

    // Minutes
    minutes = '<option value="0">00</option><option value="30">30</option>';
    $('#id_opening_minute').append($.parseHTML(minutes));
    $('#id_closing_minute').append($.parseHTML(minutes));

    // States
    state_options = '';
    for (var i in state_info) {
      state_options += '<option value="' + state_info[i] + '">'+ state_info[i] + '</option>'
    }
    $('#id_state').append($.parseHTML(state_options));
  }

  function createForm() {
    createDropdowns();
  }

  function processForm() {
    console.log('processing');
  }
}

$(document).ready(function() {
  add_zoo();
});
