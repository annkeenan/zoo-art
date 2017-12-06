function add_species(species) {
  // Store ajax response values
  var region_info;
  var habitat_info;
  var status_info;
  var family_info;

  // Start chain of ajax requests
  getRegions(species);

  // Bind the form
  $('#id_species_form').bind('submit', processForm);

  // Get a list of regions
  function getRegions() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
        response = JSON.parse(xmlHttp.response);
        if (response.result == 'success') {
          region_info = response.regions;
        } else {
          region_info = {}
        }
        getHabitats();
      }
    }
    xmlHttp.open("GET", "http://student04.cse.nd.edu:51042/region/", true);
    xmlHttp.send(null);
  }
  // Get a list of habitats
  function getHabitats() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
        response = JSON.parse(xmlHttp.response);
        if (response.result == 'success') {
          habitat_info = response.habitats;
        } else {
          habitat_info = {}
        }
        getStatuses();
      }
    }
    xmlHttp.open("GET", "http://student04.cse.nd.edu:51042/habitat/", true);
    xmlHttp.send(null);
  }
  // Get a list of Statuses
  function getStatuses() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
        response = JSON.parse(xmlHttp.response);
        if (response.result == 'success') {
          status_info = response.statuses;
        } else {
          status_info = {}
        }
        getFamilies();
      }
    }
    xmlHttp.open("GET", "http://student04.cse.nd.edu:51042/status/", true);
    xmlHttp.send(null);
  }
  // Get a list of families
  function getFamilies() {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
        response = JSON.parse(xmlHttp.response);
        if (response.result == 'success') {
          family_info = response.families;
        } else {
          family_info = {}
        }
        createForm();
      }
    }
    xmlHttp.open("GET", "http://student04.cse.nd.edu:51042/classification/", true);
    xmlHttp.send(null);
  }

  // Add links to the page
  function createDropdowns() {
    //region
    region_options = '';
    for (var i in region_info){
        region_options += '<option value="' + region_info[i] + '">'+ region_info[i] + '</option>'
    }
    $('#id_region').append($.parseHTML(region_options));
    //habitat
    habitat_options = '';
    for (var i in habitat_info){
        habitat_options += '<option value="' + habitat_info[i] + '">'+ habitat_info[i] + '</option>'
    }
    $('#id_habitat').append($.parseHTML(habitat_options));
    //status
    status_options = '';
    for (var i in status_info){
        status_options += '<option value="' + status_info[i] + '">'+ status_info[i] + '</option>'
    }
    $('#id_status').append($.parseHTML(status_options));
    //family
    family_options = '';
    for (var i in family_info){
        family_options += '<option value="' + family_info[i] + '">'+ family_info[i] + '</option>'
    }
    $('#id_family').append($.parseHTML(family_options));


  }

  function createForm() {
    createDropdowns();
    // Set dropdown values
    // Set edit text values
    /*$('#id_common_name').val(species_info.common_name);
    $('#id_genus'),val(species_info.genus);
    $('#id_family').val(species_info.family);
    $('#id_region').val(species_info.region);
    $('#id_habitat').val(species_info.habitat);
    $('#id_status').val(species_info.status);*/
  }

  function processForm() {
    species_name = $('#id_species_name').val().split(' ').join('_');
    common_name = $('#id_common_name').val().split(' ').join('_');
    var dict = JSON.stringify({
      "species": species_name,
      "info": {
        "common_name": common_name,
        "genus": $('#id_genus').val(),
        "family":$('#id_family').val(),
        "region": $('#id_region').val(),
        "habitat": $('#id_habitat').val(),
        "status": $('#id_status').val()
      }
    });

    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
        response = JSON.parse(xmlHttp.response);
        if (response.result == 'success') {
          location.href = "species.html?species=" + species_name;
        } else {
          location.href = "list_species.html";
        }

      }
    }
    xmlHttp.open("POST", "http://student04.cse.nd.edu:51042/species/", true);
    xmlHttp.send(dict);
  }
}

$(document).ready(function() {
  add_species();
});
