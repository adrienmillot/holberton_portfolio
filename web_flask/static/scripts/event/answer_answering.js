$(document).ready(function () {
	$('#btn_validate_answer').click(function () {
		$.each($('.input.checkbox_answer'), function () {
			if ($(this).is(':checked')) {
				postProposal()
			}
		})
	})
})

const postProposal = function (label, question_id, is_valid) {
	let obj = { label: label, question_id: question_id, is_valid: is_valid }
	let json_data = JSON.stringify(obj)
	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/proposals',
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
			let label = response.label
			$('section.alert_success_create_proposal').empty();
			$('section.alert_success_create_proposal').append(MessageProposalSucessCreate(label))
		}
	}
	);
}