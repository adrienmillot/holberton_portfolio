const getQuestionAnswer = function (survey_id) {

	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/surveys/' + survey_id + '/question',
		type: 'GET',
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
				default:
					window.location = "/dashboard";
					break;
			}
		},
		success: function (response) {

			$('H5#count').html("Question # " + response.count)
			$('P#question_to_answer').html(response.result.label)
			getProposalByQuestion(response.result.id)
		}
	})
}

const postProposal = function (proposal_id) {

	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/proposals/' + proposal_id + '/answers',
		type: 'POST',
		headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` },
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
			location.reload();
		}
	})
}

const getProposalByQuestion = function (question_id) {
	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/questions/' + question_id + '/proposals',
		type: 'GET',
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
			proposalListByQuestion(response);
			$('#btn_validate_answer').click(function(){
				$('input:checked').each(function (key, element) {
					proposal_id = $(this).attr('data-id');
					postProposal(proposal_id)
			})
		})
	}});
}

const proposalListByQuestion = function (proposals) {
	var i = 1;
	$.each(proposals, function (key, proposal) {

		buildDomProposal(proposal.label, i, proposal.id)
		i = i + 1
	})
}

const buildDomProposal = function (label, i, id) {
	var proposal_row = "#proposal_row_" + (i - 1);
	if (i === 1 || i % 2 != 0) {
		$('#form_proposal_answer').append(proposalColLeft(label, i, id))
	} else {
		$(proposal_row).append(proposalColRight(label, id))
	}
}

const proposalColLeft = function (label, i, id) {
	var defInput = $('<input type="checkbox" />').attr('data-id', id)
	var defProp = $('<p class="checkbox"></p>').append(defInput).append(" " + label)
	var defCol = $('<div class="col-sm-5"></div>').append(defProp)
	// var closeDiv = $('</div>')

	return $('<div class="row mt-5" id="proposal_row_' + i + '"></div>').append(defCol)
}

const proposalColRight = function (label, id) {
	var defInput = $('<input type="checkbox" />').attr('data-id', id)
	var defProp = $('<p class="checkbox" id="checkbox_1"></p>').append(defInput).append(" " + label)
	return $('<div class="col sm-5"></div>').append(defProp)
}


$(document).ready(function () {
	const url = window.location.pathname;
	const url_args = url.split('/');
	if (url_args[1] == 'surveys' && url_args[4] == 'answer') {
		const survey_id = url_args[2];
		const survey_name = url_args[3];
		getQuestionAnswer(survey_id);

	}
})
