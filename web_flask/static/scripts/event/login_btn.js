$(document).ready(function () {
	token = localStorage.getItem('token')

	if (token) {
		$("#btn_login").hide();
	
	}
	if ((!token) && (window.location != "http://0.0.0.0:5000/") && (window.location != "http://0.0.0.0:5000/login")) {
		window.location = "http://0.0.0.0:5000/"
	}
});

const redirectToLogin = function () {
	window.location = "http://0.0.0.0:5000/login"
}


$(() => {
	$('#btn_login').on('click', () => {
		redirectToLogin();
	});
});
