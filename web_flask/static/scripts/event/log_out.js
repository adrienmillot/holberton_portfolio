$(document).ready(function () {
	token = localStorage.getItem('token')

	if (!token) {
		$("#btn_logout").hide();
		$("#secure_menu").hide()
	}
});

const redirectToIndex = function () {
	localStorage.removeItem('token');
	window.location = "/"
}


$(() => {
	$('#btn_logout').on('click', () => {
		redirectToIndex();
	});
});


