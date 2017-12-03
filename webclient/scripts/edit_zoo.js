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
    // Set dropdown values
    closing_time = zoo_info.closing_time.split(':');
    $('#id_closing_hour').val(parseInt(closing_time[0]));
    $('#id_closing_minute').val(parseInt(closing_time[1]));
    opening_time = zoo_info.opening_time.split(':');
    $('#id_opening_hour').val(parseInt(opening_time[0]));
    $('#id_opening_minute').val(parseInt(opening_time[1]));
    $('#id_state').val(zoo_info.state);

    // Set edit text values
    $('#id_acres').val(zoo_info.acres);
    $('#id_address').val(zoo_info.address);
    $('#id_annual_visitors').val(zoo_info.annual_visitors);
    $('#id_city').val(zoo_info.city);
    $('#id_num_animals').val(zoo_info.num_animals);
    $('#id_website').val(zoo_info.website_url);
  }

  function processForm() {
    opening_time = $('#id_opening_hour').val() + ':' + $('#id_opening_minute').val();
    closing_time = $('#id_closing_hour').val() + ':' + $('#id_closing_minute').val();
    var dict = JSON.stringify({
      "city": $('#id_city').val(),
      "state": $('#id_state').val(),
      "address": $('#id_address').val(),
      "num_animals": $('#num_animals').val(),
      "acres": $('#id_acres').val(),
      "opening_time": opening_time,
      "closing_time": closing_time,
      "annual_visitors": $('#id_annual_visitors').val(),
      "website_url": $('#id_website').val()
    });

    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
        response = JSON.parse(xmlHttp.response);
      }
    }
    xmlHttp.open("PUT", "http://student04.cse.nd.edu:51042/zoo/" + zoo, true);
    xmlHttp.send(dict);
  }
}

$(document).ready(function() {
  let params = (new URL(document.location)).searchParams;
  let zoo = params.get("zoo");
  $('#id_title').html(zoo.split('_').join(' '));
  edit_zoo(zoo);
});
