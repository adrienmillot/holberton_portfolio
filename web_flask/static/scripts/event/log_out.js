$(document).ready(function () {
	token = localStorage.getItem('token')

	if (!token) {
		$("#btn_logout").hide();
		$("#secure_menu").hide()
	}
});

const redirectToIndex = function () {
	localStorage.removeItem('token');
	window.location = "http://0.0.0.0:5000/"
}


$(() => {
	$('#btn_logout').on('click', () => {
		redirectToIndex();
	});
});


