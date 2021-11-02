
const editUser = function (username, password, user_id) {
  const obj = {
    username: username,
    password: password
  };
  const json_data = JSON.stringify(obj);

  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/users/' + user_id,
    type: 'PUT',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    data: json_data,
    contentType: 'application/json',

    success: function (response) {
      $('section.alert_success_edit_user').empty();

      $('section.alert_success_edit_user').append(getAlertUpdateElement('Your username <strong>' + response.username + '</strong> has been well updated'));
      $('section.alert_success_edit_user').append(getAlertUpdateElement('Your password has been well updated, don\'t forget it !'));
    }
  }
  );
};

const setUserAttributes = function (user_id) {
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/users/' + user_id,
    type: 'GET',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    contentType: 'application/json',

    success: function (response) {
      $('#txt_user_name').val(response.username);
    }
  });
};

$(document).ready(function () {
  const url = window.location.pathname;
  const url_args = url.split('/');
  if (url_args[1] == 'users' && url_args[3] == 'edit') {
    const user_id = url_args[2];

    setUserAttributes(user_id);

    $('#btn_edit_user').click(function () {
      const username = $('#txt_user_name').val().trim();
      const password = $('#txt_user_password').val().trim();
	  const secure_username = username.replace(/</g, '&lt;').replace(/>/g, '&gt;');

      editUser(secure_username, password, user_id);
    });
  }
});
