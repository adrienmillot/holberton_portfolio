/**
 * get request to api to get all surveys
 */

const getProfileForCreateUser = function () {
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/profiles',
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
      profileListForUser(response.results);
    }
  });
};
function profileListForUser (profiles) {
  $.each(profiles, function (key, profile) {
    $('#select_profile').append(profileOption(profile));
  });
}

function profileOption (profile) {
  return ($('<option></option>').attr('value', profile.id).text(profile.first_name).append(' ').append(profile.last_name));
}

const createUser = function (username, password, profile_id) {
  const obj = { username: username, profile_id: profile_id, password: password };
  const json_data = JSON.stringify(obj);
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/users',
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
      const username = response.username;
      $('section.alert_success_create_user').empty();
      $('section.alert_success_create_user').append(MessageUserSucessCreate(username));
    }
  }
  );
};

function MessageUserSucessCreate (username) {
  return (`
<div class="alert alert-success" role="alert">
  You're user <strong>${username}</strong>, have been succefuly created
</div>`);
}

$(document).ready(function () {
  getProfileForCreateUser();
  $('#btn_create_user').on('click', () => {
    const username = $('#txt_user_username').val().trim();
    const password = $('#txt_user_password').val().trim();
    const profile_id = $('#select_profile').val();
    const secure_username = username.replace(/</g, '&lt;').replace(/>/g, '&gt;');

    createUser(secure_username, password, profile_id);
  });
});
