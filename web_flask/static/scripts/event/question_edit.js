
const editQuestion = function (label, question_id) {
  const obj = { label: label };
  const json_data = JSON.stringify(obj);

  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/questions/' + question_id,
    type: 'PUT',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    data: json_data,
    contentType: 'application/json',

    success: function (response) {
      $('section.alert_success_edit_question').empty();

      $('section.alert_success_edit_question').append(getAlertUpdateElement('Your question <strong>' + response.label + '</strong> has been well updated'));
    }
  }
  );
};

const setQuestionLabel = function (question_id) {
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/questions/' + question_id,
    type: 'GET',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    contentType: 'application/json',

    success: function (response) {
      $('#txt_question_label').val(response.label);
    }
  });
};

$(document).ready(function () {
  const url = window.location.pathname;
  const url_args = url.split('/');
  if (url_args[1] == 'questions' && url_args[3] == 'edit') {
    const question_id = url_args[2];

    setQuestionLabel(question_id);

    $('#btn_edit_question').click(function () {
      const label = $('#txt_question_label').val().trim();
	  const secure_label = label.replace(/</g, '&lt;').replace(/>/g, '&gt;');

      editQuestion(secure_label, question_id);
    });
  }
});
