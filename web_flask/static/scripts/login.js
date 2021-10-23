
const postLogin = function (username, password) {
	let obj = { username: username, password: password }
	let json_data = JSON.stringify(obj)
	$.ajax({
		url: 'https://ss-api.2835holberton.tech/api/v1/auth/login',
		type: 'POST',
		data: json_data,
		contentType: 'application/json',
		error: function (data) {
			dataResponse = data.responseJSON
			statusCode = data.status

			switch (statusCode) {
				case 404:
					$('section.alert_login_wrong').append(MessageWrongLogin())
		}},
			success: function (response) {
				localStorage.setItem('token', response.auth_token)
				redirectToDashboard();
		}
	});
}

function MessageWrongLogin() {
	return (`
	<div class="alert alert-warning" role="alert">
	  Wrong Username or Password
	</div>`)
}

const redirectToDashboard = function () {
	window.location = "/dashboard"
}

const redirectToSignUp = function () {
	window.location = "/sign_up"
}

$(() => {
	$('#btn_submit_login').on('click', () => {
		let username = $("#txt_uname").val().trim()	;
		let password = $("#txt_pwd").val().trim();
		postLogin(username, password);
	});

	$('#btn_sign').on('click', () => {
		redirectToSignUp();
	});
});
