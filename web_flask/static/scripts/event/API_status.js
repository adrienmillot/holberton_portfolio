/**
 * Check if the api is online or offline
 */
$(document).ready(function () {

	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/status',
		type: 'GET',
		headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` },
		error: function () {
			$('.api_status_on').hide();
		},
		success: function () {
			$('.api_status_off').hide();
		}
	});
})
