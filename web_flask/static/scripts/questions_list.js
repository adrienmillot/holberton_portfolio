/**
 * get request to api to get all questions
 */

const getQuestionsListPage = function (page) {
  const limit = 10;
  const obj = { limit: limit, page: page };

  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/questions',
    type: 'GET',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    data: obj,
    error: function (data) {
      dataResponse = data.responseJSON;
      statusCode = data.status;

      switch (statusCode) {
        case 498:
          // Remove auth_token
          localStorage.removeItem('token');
          // Redirect to homepage
          window.location = '/';
          break;
      }
    },
    success: function (response) {
      questionList(response.results);
      if (response.page_count > 1) {
        buildPaginationBtnsQuestion(response.page_count, parseInt(page));
      }
    }
  });
};
/**
 * Generate precedent link
 * Generate i times pagination links
 * Generate next link
 */
function buildPaginationBtnsQuestion (page_count, page) {
  if (page === 1 || page === undefined) {
    var previousBtnDisable = 'disabled';
  } else {
    var previousBtnDisable = '';
  }
  if (page === page_count) {
    var nextBtnDisable = 'disabled';
  } else {
    var nextBtnDisable = '';
  }

  $('ul#question_pagination').append('<li class="page-item ' + previousBtnDisable + '"><a class="page-link" id="prevBtnQuestion" tabindex="-1" aria-disabled="true">Previous</a></li>');

  for (i = 1; i <= page_count; i++) {
    $('ul#question_pagination').append($(' <li class="page-item"></li>').append(NavigationBtnQuestion(i)));
    const linkAction = $('a#' + i + '_question.page-link');
    linkAction.click(function () {
      new_page = $(this).attr('data-id');
      window.location = '/questions?page=' + new_page;
    });
  }
  $('ul#question_pagination').append('<li class="page-item ' + nextBtnDisable + '"><a class="page-link" id="nextBtnQuestion">Next</a></li>');
  $('a#prevBtnQuestion.page-link').click(function () {
    if (page !== 1) {
      window.location = '/questions?page=' + (page - 1);
    }
  });
  $('a#nextBtnQuestion.page-link').click(function () {
    if (page !== page_count) {
      window.location = '/questions?page=' + (page + 1);
    }
  });
}

function NavigationBtnQuestion (i) {
  return $('<a class="page-link" id="' + i + '_question">' + i + '</a>').attr('data-id', i);
}

/**
 * Generate DOM for show button.
 */
function questionShowButton (question) {
  return $('<button class="btn show btn-secondary btn-sm"></button>').attr('data-id', question.id).html(`
	<svg xmlns="http://www.w3.org/2000/svg"
		width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16">
		<path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z" />
		<path
			d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8zm8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z" />
	</svg>`);
}

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

/**
 * Generate DOM for action buttons.
 */
function questionActionsButton (question) {
  const showQuestionButton = questionShowButton(question);
  const editQuestionButton = questionEditButton(question);
  const deleteQuestionButton = questionDeleteButton(question);

  return $('<div class="btn-group" role="group"></div>').append(showQuestionButton).append(editQuestionButton).append(deleteQuestionButton);
}

/**
 * Generate DOM for question row.
 */
function questionRow (question, count) {
  const countTh = $('<th></th>').text('#' + count);
  const labelTd = $('<td></td>').text(question.label);
  const CategoryidTd = $('<td></td>').text(GetCategoryNameForQuestion(question.category_id));
  const SurveyidTd = $('<td></td>').text(GetSurveyNameForQuestion(question.survey_id));
  const btnActionTd = $('<td></td>').append(questionActionsButton(question));

  return $('<tr class="question"></tr>').append(countTh).append(labelTd).append(CategoryidTd).append(SurveyidTd).append(btnActionTd);
}

function GetSurveyNameForQuestion (id) {
  let name = '';

  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/surveys/' + id,
    type: 'GET',
    async: false,
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    error: function (data) {
      dataResponse = data.responseJSON;
      statusCode = data.status;

      switch (statusCode) {
        case 498:
          // Remove auth_token
          localStorage.removeItem('token');
          // Redirect to homepage
          window.location = '/';
          break;
      }
    }
  })
    .done(function (data) {
      name = (data.name);
    });
  return (name);
}

function GetCategoryNameForQuestion (id) {
  let name = '';
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/categories/' + id,
    type: 'GET',
    async: false,
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    error: function (data) {
      dataResponse = data.responseJSON;
      statusCode = data.status;

      switch (statusCode) {
        case 498:
          // Remove auth_token
          localStorage.removeItem('token');
          // Redirect to homepage
          window.location = '/';
          break;
      }
    }
  })
    .done(function (data) {
      name = (data.name);
    });
  return (name);
}

/**
 *
 */
function questionList (questions) {
  $.each(questions, function (key, question) {
    $('tbody.questions_list').append(questionRow(question, key));
  });

  btnQuestionShowEvent();
  btnQuestionEditEvent();
  btnQuestionDeleteEvent();
}

function btnQuestionShowEvent () {
  /**
	 * Click on show button
	 */
  $('.question .btn.show').click(function () {
    question_id = $(this).attr('data-id');
    window.location = '/questions/' + question_id + '/show';
  });
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

$(document).ready(function () {
  const url = window.location.pathname;
  const url_splitted = url.split('/');
  const page = $('#page_argument_question').val();
  if (url_splitted[1] == 'questions') {
    getQuestionsListPage(page);
  }
});
