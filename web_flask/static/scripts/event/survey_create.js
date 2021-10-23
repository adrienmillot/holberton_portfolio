
const createSurvey = function (name) {
	let obj = { name: name }
	let json_data = JSON.stringify(obj)
	$.ajax({
		url: 'http://ss-api.2835holberton.tech/api/v1/surveys',
		type: 'POST',
		headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` },
		data: json_data,
		contentType: 'application/json',
		error: function (data) {
			dataResponse = data.responseJSON
			statusCode = data.status

			switch (statusCode) {
				case 401:
					console.error(dataResponse.message);
					break;
			}
		},
		success: function (response) {
			let name = response.name
			$('section.alert_success_create_survey').empty();

			$('section.alert_success_create_survey').append(articleHtml(name))
		}
	}
	);
}

function articleHtml(name) {
	return (`
<div class="alert alert-success" role="alert">
  Your survey <strong>${name}</strong>, have been succefuly created
</div>`)
}

$(() => {
	$('#btn_create_survey').on('click', () => {
		let name = $("#txt_survey_name").val().trim();
		createSurvey(name);
	});
});
