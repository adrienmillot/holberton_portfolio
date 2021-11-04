const getProfile = function () {
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/me',
    type: 'GET',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },

    error: function (data) {
      dataResponse = data.responseJSON;
      statusCode = data.status;

      switch (statusCode) {
        case 498:
          localStorage.removeItem('token');
          window.location = '/';
          break;
      }
    },
    success: function (response) {
      const htmlContent = UserProfile(response);
      $(htmlContent).appendTo('.infos_user');
    }
  });
};

function UserProfile (response) {
	member_since_response = response.user.profile.created_at.split('T')
	member_since = member_since_response[0]
  return (`
	  <article>
	  <h3>Hello ${response.user.profile.first_name} !</h3>	
	  <div id='info'>
    <ul class="list-unstyled">
	  <li>First name: ${response.user.profile.first_name}</li> 
	  <li>Last name: ${response.user.profile.last_name}</li>
	  <li>Member since: ${member_since}</li>
    </ul>
	  </div>  
	  </article>`);
}

/**
 * get request to api to get all surveys
 */

const getSurveysToDo = function () {
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/surveys/unanswered',
    type: 'GET',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    success: function (response) {
      SurveyToDOList(response.results);
      $('.survey_to').click(function () {
        survey_id = $(this).attr('data-id');
        survey_name = $(this).attr('data-name');
        window.location = '/surveys/' + survey_id + '/' + survey_name + '/answer';
      });
    }
  });
};

const SurveyToDOList = function (surveys) {
  $.each(surveys, function (key, survey) {
    $('tbody.survey_to_do_list').append(SurveyToDoRow(survey));
  });
};

const SurveyToDoRow = function (survey) {
  const SurveyNameLi = $('<td ></td>').text(survey.name);
  return $('<tr class="survey_to"></tr>').append(SurveyNameLi).attr('data-id', survey.id).attr('data-name', survey.name);
};

$(document).ready(function () {
  getProfile();
  getSurveysToDo();
});
