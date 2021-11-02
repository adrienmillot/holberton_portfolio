
const postLogin = function (username, password) {
  const obj = { username: username, password: password };
  const json_data = JSON.stringify(obj);
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/auth/login',
    type: 'POST',
    data: json_data,
    contentType: 'application/json',
    error: function (data) {
      dataResponse = data.responseJSON;
      statusCode = data.status;

      switch (statusCode) {
        case 404:
          $('section.alert_login_wrong').append(MessageWrongLogin());
      }
    },
    success: function (response) {
      localStorage.setItem('token', response.auth_token);
      redirectToDashboard();
    }
  });
};

function MessageWrongLogin () {
  return (`
	<div class="alert alert-warning" role="alert">
	  Wrong Username or Password
	</div>`);
}

const redirectToDashboard = function () {
  window.location = '/dashboard';
};

const redirectToSignUp = function () {
  window.location = '/sign_up';
};

$(() => {
  $('#btn_submit_login').on('click', () => {
    const username = $('#txt_uname').val().trim();
    const password = $('#txt_pwd').val().trim();
    postLogin(username, password);
  });

  $('#btn_sign').on('click', () => {
    redirectToSignUp();
  });
});
