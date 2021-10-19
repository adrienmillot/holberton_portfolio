
const postProfile = function (first_name, last_name, gender) {
	let born_at = "1985-10-19T10:08:27.000000"
	let obj = { first_name: first_name, last_name: last_name, gender: gender, born_at: born_at }
	let json_data = JSON.stringify(obj)
	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/profiles',
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
				default:
					console.log(dataResponse)
			}
		},
		success: function (response) {
			let name = response.first_name
			$('section.alert_success_create_survey').append(articleHtml(name))
		}
	}
	);
}

function articleHtml(name) {
	return (`
<div class="alert alert-success" role="alert">
	You're profile for ${name} have been succefuly created
</div>`)
}


$(() => {
	$('#btn_create_profile').on('click', () => {
		let first_name = $("#txt_first_name").val().trim();
		let last_name = $("#txt_last_name").val().trim();
		let gender = $("#select_gender").val()
		postProfile(first_name, last_name, gender);
	});
});
