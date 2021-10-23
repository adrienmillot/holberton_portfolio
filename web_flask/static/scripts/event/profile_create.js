const createProfile = function (first_name, last_name, gender) {
	// let born_at = ""
	let obj = { first_name: first_name, last_name: last_name, gender: gender }
	let json_data = JSON.stringify(obj)
	$.ajax({
		url: 'http://ss-api.2835holberton.tech/api/v1/profiles',
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
			let FirstName = response.first_name
			$('section.alert_success_create_profile').empty();
			$('section.alert_success_create_profile').append(MessageProfileSuccessCreate(FirstName))
		}
	}
	);
}

function MessageProfileSuccessCreate(FirstName) {
	return (`
<div class="alert alert-success" role="alert">
  Your profile for <strong>${FirstName}</strong>, have been succefuly created
</div>`)
}

$(document).ready( function () {
	$('#btn_create_profile').on('click', () => {
		let first_name = $("#txt_profile_first_name").val().trim();
		let last_name = $("#txt_profile_last_name").val().trim()
		let gender = $("#select_gender_for_profile").val()
		createProfile(first_name, last_name, gender);
	});
});
