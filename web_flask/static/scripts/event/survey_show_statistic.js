const GraphCategories = function (result) {

	let labels = []
	let categoriesData = []

	result.survey.labels.forEach(element => {
		labels.push(element)
	});

	result.survey.user_score.forEach(element => {
		categoriesData.push(parseFloat(element))
	});

	const data = {
		labels: labels,
		datasets: [{
			label: 'Categories Dataset',
			backgroundColor: 'rgba(255, 193, 7, 0.5)',
			borderColor: 'rgb(255, 193, 7)',
			data: categoriesData,
		}]
	};

	const config = {
		type: 'radar',
		data: data,
		options: {
			scales: {
				r: {
					suggestedMin: 0,
				}
			}
		}
	};

	const ScoreSurveyCategoriesChart = new Chart(
		document.getElementById('ScoreSurveyCategoriesChart'),
		config
	);

};

const GraphQuestions = function (result) {

	let labels = []
	let questionsData = []

	result.survey.labels.forEach(element => {
		labels.push(element)
	});

	result.survey.user_scores.forEach(element => {
		questionsData.push(parseFloat(element))
	});

	const data = {
		labels: labels,
		datasets: [{
			label: 'Questions dataset',
			backgroundColor: 'rgba(255, 193, 7)',
			borderColor: 'rgb(255, 193, 7)',
			data: questionsData,
		}]
	};

	const config = {
		type: 'bar',
		data: data,
		options: {}
	};

	const ScoreSurveyQuestionsChart = new Chart(
		document.getElementById('ScoreSurveyQuestionsChart'),
		config
	);

};

const ResultCategories = function (survey_id) {
	let limit = 8
	let obj = { limit: limit}
	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/surveys/' + survey_id + '/categories_score',
		type: 'GET',
		headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` },
		data: obj,
		error: function (data) {
			dataResponse = data.responseJSON;
			statusCode = data.status;
			switch (statusCode) {
				case 498:
					localStorage.removeItem('token');
					window.location = "/";
					break;
			}
		},
		success: function (response) {
			GraphCategories(response)
		}
	});
}

const ResultSurvey = function (survey_id) {
	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/surveys/' + survey_id + '/score',
		type: 'GET',
		headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` },
		error: function (data) {
			dataResponse = data.responseJSON;
			statusCode = data.status;
			switch (statusCode) {
				case 498:
					localStorage.removeItem('token');
					window.location = "/";
					break;
			}
		},
		success: function (response) {
			const htmlContent = SurveyScore(response.message);
			$(htmlContent).appendTo('.infos_Survey_Score');
		}
	});
}

const SurveyScore = function (score) {
	return(`
	<article>
	<h3>${score}</h3>
	</article>
	`)

}

const ResultQuestions = function (survey_id) {
	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/surveys/' + survey_id + '/question_score',
		type: 'GET',
		headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` },
		error: function (data) {
			dataResponse = data.responseJSON;
			statusCode = data.status;
			switch (statusCode) {
				case 498:
					localStorage.removeItem('token');
					window.location = "/";
					break;
			}
		},
		success: function (response) {
			GraphQuestions(response)
		}
	});
}

window.onload = function () {
	var url = window.location.pathname;
	var url_splitted = url.split('/')

	if (url_splitted[1] == 'surveys' && url_splitted[3] == 'show') {
		var survey_id = url_splitted[2];

		ResultSurvey(survey_id);
		ResultCategories(survey_id);
		ResultQuestions(survey_id);
	}
}