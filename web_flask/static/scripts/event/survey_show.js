$(document).ready(function () {
	var url = window.location.pathname;
	var url_splitted = url.split('/')

	if (url_splitted[1] == 'surveys' && url_splitted[3] == 'show') {
		var survey_id = url_splitted[2];
		$.ajaxSetup({
			headers: {
				'Authorization': `Bearer ${localStorage.getItem('token')}`
			}
		});

		$.get('http://ss-api.2835holberton.tech/api/v1/surveys/' + survey_id, function (data) {
      btn_delete = surveyDeleteButton(data);
      btn_edit = surveyEditButton(data);
      bts = $('<div class="btn-group float-right survey"></div>').append(btn_edit).append(btn_delete);
			$('body > .container-fluid > h1').text(data.name).append(bts);
      btnSurveyEditEvent();
      btnSurveyDeleteEvent();
		});
	}
});
