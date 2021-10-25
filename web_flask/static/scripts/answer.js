const getQuestionAnswer = function (survey_id) {

	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/surveys/' + survey_id + '/question',
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
			$('P#question_to_answer').html(response.label)
			getProposalByQuestion(response.id)
	
		}
	});
}

const getProposalByQuestion = function (question_id) {

	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/questions/' + question_id + '/proposals',
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
			console.log(response);
			proposalListByQuestion(response, response.length);
		}
	});
}

const proposalListByQuestion = function (proposals, nbr_proposals) {
	var i = 1;
	$.each(proposals, function (key, proposal) {
	
		buildDomProposal(proposal.label, i, proposal.id)
		i = i + 1
	})
}

const buildDomProposal = function (label, i, id) {
	var proposal_row = "#proposal_row_" + (i - 1);
	 if (i === 1 || i % 2 != 0 ) {
		$('#form_proposal_answer').append(proposalColLeft(label ,i, id))
	 } else {
		 console.log(proposal_row)
		$(proposal_row).append(proposalColRight(label, i, id))
	 }
}

const proposalColLeft = function (label, i, id) {
	console.log(i)
	
	var defInput = $('<input class="checkbox_answer" type="checkbox" name="checkbox_answer_' + i + '" id="checkbox_answer_' + i + '" />').attr('data-id', id)
	var defProp = $('<p class="checkbox"></p>').append(defInput).append(label)
	var defCol = $('<div class="col-sm-5"></div>').append(defProp)
	// var closeDiv = $('</div>')
	
	return $('<div class="row mt-5" id="proposal_row_' + i + '"></div>').append(defCol)
}

const proposalColRight =function (label, i, id) {
	console.log(i)
	var defInput = $('<input class="checkbox_answer" type="checkbox" name="checkbox_answer_' + i + '" id="checkbox_answer_' + i + '" />').attr('data_id', id)
	var defProp = $('<p class="checkbox" id="checkbox_1"></p>').append(defInput).append(label)
	return $('<div class="col sm-5"></div>').append(defProp)
}


$(document).ready(function () {
	const url = window.location.pathname;
	const url_args = url.split('/');
	if (url_args[1] == 'surveys' && url_args[4] == 'answer') {
		  const survey_id = url_args[2];
		  const survey_name = url_args[2];
		  getQuestionAnswer(survey_id);
		  
	}})
