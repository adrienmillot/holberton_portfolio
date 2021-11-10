$(document).ready(function () {
  const url = window.location.pathname;
  const url_splitted = url.split('/');

  if (url_splitted[1] == 'surveys' && url_splitted[3] == 'show') {
    const survey_id = url_splitted[2];
    $.ajaxSetup({
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });

    $.get('http://0.0.0.0:5002/api/v1/surveys/' + survey_id, function (data) {
      btn_delete = surveyDeleteButton(data);
      btn_edit = surveyEditButton(data);
      bts = $('<div class="btn-group float-right survey"></div>').append(btn_edit).append(btn_delete);
      $('body > .container-fluid > h1').text(data.name).append(bts);
      btnSurveyEditEvent();
      btnSurveyDeleteEvent();
    });
  }
});

function surveyDeleteButton (survey) {
  return $('<button class="btn delete btn-secondary btn-sm"></button>').attr('data-id', survey.id).html(`<svg xmlns="http://www.w3.org/2000/svg"
	width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
	<path
		d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z" />
</svg>`);
}

function surveyEditButton (survey) {
  return $('<button class="btn edit btn-secondary btn-sm"></button>').attr('data-id', survey.id).html(`<svg xmlns="http://www.w3.org/2000/svg"
	width="16" height="16" fill="currentColor" class="bi bi-pencil-square"
	viewBox="0 0 16 16">
	<path
		d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z" />
	<path fill-rule="evenodd"
		d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z" />
</svg>`);
}

function btnSurveyEditEvent () {
  $('.survey .btn.edit').click(function () {
    survey_id = $(this).attr('data-id');
    window.location = '/surveys/' + survey_id + '/edit';
  });
}

function btnSurveyDeleteEvent () {
  $('.survey .btn.delete').click(function () {
    survey_id = $(this).attr('data-id');
    delet = deleteActionSurvey(survey_id);
    if (delet = true) {
      $(this).parent().parent().parent().remove();
    }
  });
}
function deleteActionSurvey (id) {
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/surveys/' + id,
    type: 'DELETE',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    error: function (data) {
      dataResponse = data.responseJSON;
      statusCode = data.status;

      switch (statusCode) {
        case !200:
          console.error(dataResponse.message);
          break;
      }
    },
    success: function (data) {
      $(document).ready(function () {
        $('section.alert_success_delete_survey').empty();
        $('section.alert_success_delete_survey').append(MessageConfirmationDeleteSurvey());
        return (true);
      });
    }
  });
}

function MessageConfirmationDeleteSurvey () {
  return (`
	<div class="alert alert-success" role="alert">
	  Your survey, have been succefuly deleted
	</div>`);
}
