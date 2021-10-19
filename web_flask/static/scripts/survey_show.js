$(document).ready(function () {
  var url = window.location.pathname;
  var url_splitted = url.split('/')
  var survey_id = url_splitted[2];

  $.ajaxSetup({
    headers: {
      'Authorization': `Bearer ${localStorage.getItem('token')}`
    }
  });

  $.get('http://0.0.0.0:5002/api/v1/surveys/'+survey_id, function(data) {
    $('body > .container-fluid > h1').text(data.name)
  });
});
