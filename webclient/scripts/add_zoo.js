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
        state_info = JSON.parse(xmlHttp.response);
        createForm(response);
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
    minutes = '<option value="0">00</option><option value="30">30</option>';
    $('#id_open_minute').append($.parseHTML(minutes));
    $('#id_close_minute').append($.parseHTML(minutes));

    // States
    state_options = '';
    for (var i in states.states) {
      state_options += '<option value="' + states.states[i] + '">'+ states.states[i] + '</option>'
    }
    $('#id_state').append($.parseHTML(state_options));
  }

  function createForm(states) {
    createDropdowns(states);
  }

  function processForm() {
    console.log('processing');
  }
}

$(document).ready(function() {
  add_zoo();
});
