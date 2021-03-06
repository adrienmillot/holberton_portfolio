
/**
 * get request to api to get all categorys
 */
const getCategoryList = function () {
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/categories',
    type: 'GET',
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
    },
    success: function (response) {
      categoryList(response.results);
    }
  });
};

function categoryList (categorys) {
  $.each(categorys, function (key, category) {
    $('#select_category').append(categoryOption(category));
  });
}

function categoryOption (category) {
  return ($('<option></option>').attr('value', category.id).text(category.name));
}

/**
 * get request to api to get all surveys
 */

const getSurveysForCreateQuestion = function () {
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/surveys',
    type: 'GET',
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
    },
    success: function (response) {
      surveyListForQuestion(response.results);
    }
  });
};
function surveyListForQuestion (surveys) {
  $.each(surveys, function (key, survey) {
    $('#select_survey').append(surveyOption(survey));
  });
}

function surveyOption (survey) {
  return ($('<option></option>').attr('value', survey.id).text(survey.name));
}

const createQuestion = function (label, category_id, survey_id) {
  const obj = { label: label, category_id: category_id, survey_id: survey_id };
  const json_data = JSON.stringify(obj);
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/questions',
    type: 'POST',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    data: json_data,
    contentType: 'application/json',
    error: function (data) {
      dataResponse = data.responseJSON;
      statusCode = data.status;

      switch (statusCode) {
        case 401:
          console.error(dataResponse.message);
          break;
      }
    },
    success: function (response) {
      const label = response.label;
      $('section.alert_success_create_question').empty();
      $('section.alert_success_create_question').append(MessageQuestionSuccessCreate(label));
    }
  }
  );
};

function MessageQuestionSuccessCreate (label) {
  return (`
<div class="alert alert-success" role="alert">
  Your question <strong>${label}</strong>, have been succefuly created
</div>`);
}

$(document).ready(function () {
  getCategoryList();
  getSurveysForCreateQuestion();
  $('#btn_create_question').on('click', () => {
    const label = $('#txt_question_label').val().trim();
    const category_id = $('#select_category').val();
    const survey_id = $('#select_survey').val();
    const secure_label = label.replace(/</g, '&lt;').replace(/>/g, '&gt;');

    createQuestion(secure_label, category_id, survey_id);
  });
});
