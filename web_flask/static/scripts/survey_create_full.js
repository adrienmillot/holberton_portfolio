$(document).ready(function () {
	getSurvey();
	getCategory();
	$('#btn_Next').click(function () {
		survey_id = postSurvey();
		category_id = postCategory();
		$('.survey_and_category').hide();
		$('.buton_add_question').append(btnAddQuestion())
		$('#add_question').click(function () {
			console.log("add question")
			$('.question_proposal').append(addQuestionInput(survey_id, category_id));
			$('#validate_question').click(function () {
				$('.question_input').hide()
				question_id = postQuestion(survey_id, category_id);
				console.log('question id :', question_id)
		})
	})
	
	})
})
// 	$('#add_proposal').click(function () {
// 		console.log("add proposal")
// 		// $('.').append(addProposalInput());
// 	})


// })

const postQuestion = function (survey_id, category_id) {
	const label = $('#txt_question_label').val().trim();
	const secure_label = label.replace(/</g, '&lt;').replace(/>/g, '&gt;');

	const obj = { label: secure_label, category_id: category_id, survey_id: survey_id };
	const json_data = JSON.stringify(obj);
	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/questions',
		type: 'POST',
		headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
		data: json_data,
		contentType: 'application/json',
		error: function (data) {
			dataResponse = data.responseJSON;
			statusCode = data.status;

			switch (statusCode) {
				case 401:
					console.error(dataResponse.message);
					break;
			}
		},
		success: function (response) {
			console.log(response)
			$('.question_proposal').append('<h3>' + response.label + '</h3>').append(btnProposal());
			return (response.id)
			// const label = response.label;

		}
	})
}

const btnProposal = function () {
	return (`
	<div class="col-sm-6">
<div class="btn-group">
	<input class="btn add-proposal btn-secondary btn-sm float-right" type="button"
		id="add_proposal" value="Add Proposal">
</div>
</div>
	`)
}


const btnAddQuestion = function () {
	return (`<div class="col-sm-7">
<div class="btn-group">
	<input class="btn add-question btn-secondary btn-sm float-right" type="button"
		id="add_question" value="Add Question">
</div>
</div>`)
}

const getSurvey = function () {
	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/surveys',
		type: 'GET',
		headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
		error: function (data) {
			dataResponse = data.responseJSON;
			statusCode = data.status;

			switch (statusCode) {
				case 498:
					// Remove auth_token
					localStorage.removeItem('token');
					// Redirect to homepage
					window.location = '/';
					break;
			}
		},
		success: function (response) {
			surveyList(response.results);
		}
	});
};

function surveyList(surveys) {
	$.each(surveys, function (key, survey) {
		$('#select_survey').append(surveyOption(survey));
	});
}

function surveyOption(survey) {
	return ($('<option></option>').attr('value', survey.id).text(survey.name));
}



const getCategory = function () {
	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/categories',
		type: 'GET',
		headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
		error: function (data) {
			dataResponse = data.responseJSON;
			statusCode = data.status;

			switch (statusCode) {
				case 498:
					// Remove auth_token
					localStorage.removeItem('token');
					// Redirect to homepage
					window.location = '/';
					break;
			}
		},
		success: function (response) {
			categoryList(response.results);
		}
	});
}
function categoryList(categorys) {
	$.each(categorys, function (key, category) {
		$('#select_category').append(categoryOption(category));
	});
}

function categoryOption(category) {
	return ($('<option></option>').attr('value', category.id).text(category.name));
}



const postSurvey = function () {
	const name = $('#txt_survey_name').val().trim();
	const secure_name = name.replace(/</g, '&lt;').replace(/>/g, '&gt;');
	if (secure_name !== "") {
		const obj = { name: secure_name };
		const json_data = JSON.stringify(obj);
		$.ajax({
			url: 'http://0.0.0.0:5002/api/v1/surveys',
			type: 'POST',
			headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
			data: json_data,
			contentType: 'application/json',
			error: function (data) {
				dataResponse = data.responseJSON;
				statusCode = data.status;

				switch (statusCode) {
					case 401:
						console.error(dataResponse.message);
						break;
				}
			},
			success: function (response) {
				const survey_id = response.id
				$('.survey_name').append('<h1>Survey\'s Name: ' + response.name + '</h1>')
				return (survey_id)

			}
		}
		);
	} else {
		const survey_id = $('#select_survey').val();
		const survey_name = getSurveyName(survey_id)

		return (survey_id)

	};
}

const getSurveyName = function (survey_id) {
	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/surveys/' + survey_id,
		type: 'GET',
		headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
		error: function (data) {
			dataResponse = data.responseJSON;
			statusCode = data.status;

			switch (statusCode) {
				case 498:
					// Remove auth_token
					localStorage.removeItem('token');
					// Redirect to homepage
					window.location = '/';
					break;
			}
		},
		success: function (response) {
			$('.survey_name').append('<h1>Survey\'s Name: ' + response.name + '</h1>')

		}
	});
}




const postCategory = function () {
	const name = $('#txt_category_name').val().trim();
	const secure_name = name.replace(/</g, '&lt;').replace(/>/g, '&gt;');
	if (secure_name !== '') {
		const obj = { name: secure_name };
		const json_data = JSON.stringify(obj);
		$.ajax({
			url: 'http://0.0.0.0:5002/api/v1/categories',
			type: 'POST',
			headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
			data: json_data,
			contentType: 'application/json',
			error: function (data) {
				dataResponse = data.responseJSON;
				statusCode = data.status;

				switch (statusCode) {
					case 401:
						console.error(dataResponse.message);
						break;
				}
			},
			success: function (response) {
				const category_id = response.id

				$('.category_name').append('<h2>Category\'s: ' + response.name + '</h2>')
				return (category_id)

			}
		}
		);

	} else {
		const category_id = $('#select_category').val();
		const category_name = getCategoryName(category_id)

		return (category_id)

	}
}

const getCategoryName = function (category_id) {
	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/categories/' + category_id,
		type: 'GET',
		headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
		error: function (data) {
			dataResponse = data.responseJSON;
			statusCode = data.status;

			switch (statusCode) {
				case 498:
					// Remove auth_token
					localStorage.removeItem('token');
					// Redirect to homepage
					window.location = '/';
					break;
			}
		},
		success: function (response) {

			$('.category_name').append('<h2>Category\'s: ' + response.name + '</h2>')
		}
	});
}

const addQuestionInput = function (survey_id, category_id) {
	return (`
	<div class="question_input">
	<div class="row mt-2">
		<div class="col-sm-5">
			<input class="form-control" type="text" placeholder="Question label"
				name="txt_question_label" id="txt_question_label" survey-id="${(survey_id)}" category-id="${(category_id)}"/>
		</div>
		<div class="col-sm-6">
			<input class="btn add-question btn-secondary btn-sm float-right" type="button" id="validate_question" value="Validate Question">
		</div>
		</div>
		</div>`)
}
	// 	<div class="col-sm-7">
	// 		<div class="btn-group">

	// 			<input class="btn add-question btn-secondary btn-sm float-right" type="button"
	// 			id="add_proposal" value="Add Proposal">

	// 		</div>
	// 	</div>
	// </div>
	// <!-- proposal to question -->
	// <div class="row justify-content-center">
	// 	<div class="col">
	// 		<input class="form-control" type="text" placeholder="Label"
	// 			name="txt_proposal_label" id="txt_proposal_label" />
	// 	</div>
	// 	<div class="col">
	// 		<h6> <input class="checkbox_is_valid" type="checkbox" name="checkbox_is_valid"
	// 				id="checkbox_is_valide" /> It's a valid proposal</h6>
	// 	</div>
	// </div>
	// <!-- end proposal to question -->
	// <!-- proposal to question -->
	// <div class="row justify-content-center">
	// 	<div class="col">
	// 		<input class="form-control" type="text" placeholder="Label"
	// 			name="txt_proposal_label" id="txt_proposal_label" />
	// 	</div>
	// 	<div class="col">
	// 		<h6> <input class="checkbox_is_valid" type="checkbox" name="checkbox_is_valid"
	// 				id="checkbox_is_valide" /> It's a valid proposal</h6>
	// 	</div>
	// </div>



// const addProposalInput = function () {
// 	return (``)
// }