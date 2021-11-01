/**
 * get request to api to get all questions
 */

 const getQuestionForCreateUser = function () {

	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/questions',
		type:'GET',
		headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` },
		error: function (data) {
			dataResponse = data.responseJSON
			statusCode = data.status

			switch (statusCode) {
				case 498:
					// Remove auth_token
					localStorage.removeItem('token');	
					// Redirect to homepage
					window.location = "/";
					break;
			}
		},
		success: function (response) {
			questionListForProposal(response.results);
		}
	});
}
function questionListForProposal(questions) {
	$.each(questions, function (key, question) {
		$('#select_question_for_proposal').append(questionOption(question));
	});
}

function questionOption(question) {

	return ($('<option></option>').attr('value', question.id).text(question.label))
}



const createProposal = function (label, question_id, is_valid) {
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

function MessageProposalSucessCreate(label) {
	return (`
<div class="alert alert-success" role="alert">
  Your proposal <strong>${label}</strong>, have been succefuly created
</div>`)
}

$(document).ready( function () {
	getQuestionForCreateUser();
	$('#btn_create_proposal').on('click', () => {
		let label = $("#txt_proposal_label").val().trim()
		let question_id = $("#select_question_for_proposal").val()
		let is_valid = ""
		if($('input.checkbox_is_valid').is(':checked')){
			is_valid = true
		} else {
			is_valid = false
			
		}
		let secure_label = label.replace(/</g, "&lt;").replace(/>/g, "&gt;");

		createProposal(secure_label, question_id, is_valid);
	});
});
