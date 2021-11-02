
const editSurvey = function (name, survey_id) {
  const obj = { name: name };
  const json_data = JSON.stringify(obj);

  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/surveys/' + survey_id,
    type: 'PUT',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    data: json_data,
    contentType: 'application/json',

    success: function (response) {
      $('section.alert_success_edit_survey').empty();

      $('section.alert_success_edit_survey').append(getAlertUpdateElement('Your survey <strong>' + response.name + '</strong> has been well updated'));
    }
  }
  );
};

function getAlertUpdateElement (message) {
  return $('<div class="alert alert-success" role="alert"></div>').html(message);
}

const setSurveyName = function (survey_id) {
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/surveys/' + survey_id,
    type: 'GET',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    contentType: 'application/json',

    success: function (response) {
      $('#txt_survey_name').val(response.name);
    }
  });
};

$(document).ready(function () {
  const url = window.location.pathname;
  const url_args = url.split('/');
  if (url_args[1] == 'surveys' && url_args[3] == 'edit') {
		const survey_id = url_args[2];

		setSurveyName(survey_id);
  
  $('#btn_edit_survey').click(function () {
    const name = $('#txt_survey_name').val().trim();
	let secure_name = name.replace(/</g, "&lt;").replace(/>/g, "&gt;");

    editSurvey(secure_name, survey_id);
  });
}
});
