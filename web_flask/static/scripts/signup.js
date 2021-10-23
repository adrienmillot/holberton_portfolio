$(document).ready(function () {
	$("#btn_submit").click(function () {
		var username = $("#txt_uname").val().trim();
		var password = $("#txt_pwd").val().trim();

		$.ajax({
			url: 'http://ss-api.2835holberton.tech/api/v1/auth/login',
			type: 'POST',
			data: {username: username, password: password},
			headers: {'Content-Type': 'application/json'},
			error: function (data) {
				dataResponse = data.responseJSON
				statusCode = data.status

				switch (statusCode) {
					case 400:
						console.error(dataResponse.message);
						break;
					default:
						console.log(data);
						break;
			}},
				success: function (response) {
					console.log('Succsess!', response)
					console.log('katchedToken:', response.token)
					//localStorage.setItem('token', response.token)
				}
			});
	}
	);
});
