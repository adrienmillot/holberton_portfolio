const getProfile = function () {
	$.ajax({
		url: 'https://ss-api.2835holberton.tech/api/v1/profiles',
		type: 'GET',
		headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` },

		error: function (data) {
			dataResponse = data.responseJSON
			statusCode = data.status


			switch (statusCode) {
				case 498:
					localStorage.removeItem('token')
					window.location = "/"
					break;
			}
		},
		success: function (response) {
			response.results.forEach(element => {
				if (element.first_name === "admin") {
					const htmlContent = UserProfile(element);
					$(htmlContent).appendTo('.infos_user');
				}


			});

		}
	});
}

function UserProfile(element) {
	return (`
	  <article>
	  <h3>Hello ${element.first_name} !</h3>	
	  <div id='info'>
    <ul class="list-unstyled">
	  <li>First name:${element.first_name}</li> 
	  <li>Last name: ${element.last_name}</li>
	  <li>Member since ${element.created_at}</li>
    </ul>
	  </div>  
	  </article>`)
}

/**
 * get request to api to get all surveys
 */

const getSurveysToDo = function () {

	$.ajax({
		url: 'https://ss-api.2835holberton.tech/api/v1/surveys',
		type: 'GET',
		headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` },
		success: function (response) {

			SurveyToDOList(response.results);
			$('.survey_to').click(function () {
				survey_id = $(this).attr('data-id');
				survey_name = $(this).attr('data-name');
				window.location = '/surveys/' + survey_id + '/' + survey_name + '/answer'
				console.log('select')
			});
		}
	})
}


const SurveyToDOList = function (surveys) {
	$.each(surveys, function (key, survey) {
		$('tbody.survey_to_do_list').append(SurveyToDoRow(survey));
	});
}

const SurveyToDoRow = function (survey) {
	var SurveyNameLi = $('<td ></td>').text(survey.name);
	return $('<tr class="survey_to"></tr>').append(SurveyNameLi).attr('data-id', survey.id).attr('data-name', survey.name)

}

$(document).ready(function () {
	getProfile();
	getSurveysToDo();
});

