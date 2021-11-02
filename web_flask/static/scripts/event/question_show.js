$(document).ready(function () {
  const url = window.location.pathname;
  const url_splitted = url.split('/');

  if (url_splitted[1] == 'questions' && url_splitted[3] == 'show') {
    const question_id = url_splitted[2];
    $.ajaxSetup({
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    });

    $.get('http://0.0.0.0:5002/api/v1/questions/' + question_id, function (data) {
      btn_delete = questionDeleteButton(data);
      btn_edit = questionEditButton(data);
      bts = $('<div class="btn-group float-right question"></div>').append(btn_edit).append(btn_delete);
      $('body > .container-fluid > h1').text(data.label).append(bts);
      btnQuestionEditEvent();
      btnQuestionDeleteEvent();

      $labels = $('<div id="labels"></div>');
      $('body > .container-fluid').append($labels);

      $.get('http://0.0.0.0:5002/api/v1/categories/' + data.category_id, function (data) {
        $label = $('<span></span>').attr('class', 'badge badge-secondary mr-1').text(data.name);
        $labels.append($label);
      });

      $.get('http://0.0.0.0:5002/api/v1/surveys/' + data.survey_id, function (data) {
        $label = $('<span></span>').attr('class', 'badge badge-info').text(data.name);
        $labels.append($label);
      });
    });
  }
});

/**
 * Generate DOM for edit button.
 */
function questionEditButton (question) {
  return $('<button class="btn edit btn-secondary btn-sm"></button>').attr('data-id', question.id).html(`<svg xmlns="http://www.w3.org/2000/svg"
	width="16" height="16" fill="currentColor" class="bi bi-pencil-square"
	viewBox="0 0 16 16">
	<path
		d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z" />
	<path fill-rule="evenodd"
		d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z" />
</svg>`);
}

/**
 * Generate DOM for delete button.
 */
function questionDeleteButton (question) {
  return $('<button class="btn delete btn-secondary btn-sm"></button>').attr('data-id', question.id).html(`<svg xmlns="http://www.w3.org/2000/svg"
	width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
	<path
		d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z" />
</svg>`);
}

function btnQuestionEditEvent () {
  /**
	 * Click on edit button
	 */
  $('.question .btn.edit').click(function () {
    question_id = $(this).attr('data-id');
    window.location = '/questions/' + question_id + '/edit';
  });
}

function btnQuestionDeleteEvent () {
  /**
	 * Click on delete button
	 */
  $('.question .btn.delete').click(function () {
    question_id = $(this).attr('data-id');
    delet = deleteActionQuestion(question_id);
    if (delet = true) {
      $(this).parent().parent().parent().remove();
    }
  });
}

function deleteActionQuestion (id) {
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/questions/' + id,
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
        $('section.alert_success_delete_question').empty();
        $('section.alert_success_delete_question').append(MessageConfirmationQuestion());
        return (true);
      });
    }
  });
}

function MessageConfirmationQuestion () {
  return (`
	<div class="alert alert-success" role="alert">
	  Your question, have been succefuly deleted
	</div>`);
}
