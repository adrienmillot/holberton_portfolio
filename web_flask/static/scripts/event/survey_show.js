$(document).ready(function() {
	id = localStorage.getItem('show_survey_id')
	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/surveys/' + id,
		type: 'GET',
		headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` },
		error: function (data) {
			dataResponse = data.responseJSON
			statusCode = data.status

			switch (statusCode) {
				case 400:
					console.error(dataResponse.message);
					break;
				case 498:
					// Remove auth_token
					localStorage.removeItem('token');

					// Redirect to homepage
					window.location = "/";
					break;
			}
		},
		success: function (response) {
			console.log(response.name);
			localStorage.removeItem('show_survey_id')
		}
	})
})
