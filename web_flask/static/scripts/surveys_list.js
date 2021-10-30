/**
 * get request to api to get all surveys
 */

const getSurveysListPage = function (page) {
	let limit = 10
	let obj = { limit: limit, page: page }

	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/surveys',
		type: 'GET',
		headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` },
		data: obj,
		error: function (data) {
			dataResponse = data.responseJSON
			statusCode = data.status

			switch (statusCode) {
				case 498:
					// Remove auth_token
					localStorage.removeItem('token');
					// Redirect to homepage
					window.location = "/";
					break;
			}
		},
		success: function (response) {
			surveyList(response.results);
			if (response.page_count > 1) {
				buildPaginationBtnsSurvey(response.page_count, parseInt(page))
			}
		}
	});
}
/** 
 * Generate precedent link
 * Generate i times pagination links
 * Generate next link
 */
function buildPaginationBtnsSurvey(page_count, page) {
	if (page === 1 || page === undefined) {
		var previousBtnDisable = 'disabled'
	} else {
		var previousBtnDisable = ''
	}
	if (page === page_count) {
		var nextBtnDisable = 'disabled'
	} else {
		var nextBtnDisable = ''
	}

	$('ul#survey_pagination').append('<li class="page-item ' + previousBtnDisable + '"><a class="page-link" id="prevBtnSurvey" tabindex="-1" aria-disabled="true">Previous</a></li>')

	for (i = 1; i <= page_count; i++) {
		$('ul#survey_pagination').append($(' <li class="page-item"></li>').append(NavigationBtnSurvey(i)))
		var linkAction = $('a#' + i + '_survey.page-link')
		linkAction.click(function () {
			new_page = $(this).attr('data-id')
			window.location = '/surveys?page=' + new_page
		})
	}
	$('ul#survey_pagination').append('<li class="page-item ' + nextBtnDisable + '"><a class="page-link" id="nextBtnSurvey">Next</a></li>')
	$('a#prevBtnSurvey.page-link').click(function () {
		if (page !== 1) {
			window.location = '/surveys?page=' + (page - 1)
		}
	});
	$('a#nextBtnSurvey.page-link').click(function () {
		if (page !== page_count) {
			window.location = '/surveys?page=' + (page + 1)
		}
	})
}


function NavigationBtnSurvey(i) {
	return $('<a class="page-link" id="' + i + '_survey">' + i + '</a>').attr('data-id', i)
}



/**
 * Generate DOM for show button.
 */
function surveyShowButton(survey) {
	return $('<button class="btn show btn-secondary btn-sm"></button>').attr('data-id', survey.id).html(`
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
function surveyEditButton(survey) {
	return $('<button class="btn edit btn-secondary btn-sm"></button>').attr('data-id', survey.id).html(`<svg xmlns="http://www.w3.org/2000/svg"
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
function surveyDeleteButton(survey) {
	return $('<button class="btn delete btn-secondary btn-sm"></button>').attr('data-id', survey.id).html(`<svg xmlns="http://www.w3.org/2000/svg"
	width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
	<path
		d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z" />
</svg>`);
}

/**
 * Generate DOM for action buttons.
 */
function surveyActionsButton(survey) {
	var showSurveyButton = surveyShowButton(survey);
	var editSurveyButton = surveyEditButton(survey);
	var deleteSurveyButton = surveyDeleteButton(survey);

	return $('<div class="btn-group" role="group"></div>').append(showSurveyButton).append(editSurveyButton).append(deleteSurveyButton);
}

/**
 * Generate DOM for survey row.
 */
function surveyRow(survey, count) {
	var countTh = $('<th></th>').text('#' + count);
	var nameTd = $('<td></td>').text(survey.name);
	var idTd = $('<td></td>').text(survey.id);
	var btnActionTd = $('<td></td>').append(surveyActionsButton(survey));

	return $('<tr class="survey"></tr>').append(countTh).append(nameTd).append(idTd).append(btnActionTd);
}

/**
 * 
 */
function surveyList(surveys) {
	$.each(surveys, function (key, survey) {
		$('tbody.surveys_list').append(surveyRow(survey, key));
	});

	btnSurveyShowEvent();
	btnSurveyEditEvent();
	btnSurveyDeleteEvent();
}

function btnSurveyShowEvent() {
	/**
	 * Click on show button
	 */
	$('.survey .btn.show').click(function () {
		survey_id = $(this).attr('data-id');
		window.location = '/surveys/' + survey_id + '/show'


	});

}

function btnSurveyEditEvent() {
	/**
	 * Click on edit button
	 */
	$('.survey .btn.edit').click(function () {
		survey_id = $(this).attr('data-id');
		window.location = '/surveys/' + survey_id + '/edit'
	});

}

function btnSurveyDeleteEvent() {
	/**
	 * Click on delete button
	 */
	$('.survey .btn.delete').click(function () {
		survey_id = $(this).attr('data-id');
		delet = deleteActionSurvey(survey_id);
		if (delet = true) {
			$(this).parent().parent().parent().remove()
		}
	})
};


function deleteActionSurvey(id) {

	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/surveys/' + id,
		type: 'DELETE',
		headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` },
		error: function (data) {
			dataResponse = data.responseJSON
			statusCode = data.status

			switch (statusCode) {
				case !200:
					console.error(dataResponse.message);
					break;
			}
		},
		success: function (data) {
			$(document).ready(function () {
				$('section.alert_success_delete_survey').empty();
				$('section.alert_success_delete_survey').append(MessageConfirmationDeleteSurvey())
				return (true)
			})
		}
	})
}

function MessageConfirmationDeleteSurvey() {
	return (`
	<div class="alert alert-success" role="alert">
	  Your survey, have been succefuly deleted
	</div>`)
}

$(document).ready(function () {
	var page = $('#page_argument_survey').val()
	getSurveysListPage(page);
});
