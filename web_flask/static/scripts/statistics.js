const GraphUserCategories = function (result) {
	
    let labels = []
	let categoriesData = []
	
    result.labels.forEach(element => {
            labels.push(element)
    });

    result.user_score.forEach(element => {
            categoriesData.push(parseFloat(element))
    });

    const data = {
        labels: labels,
        datasets: [{
            label: 'User Categories Dataset',
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

    const userCategoriesChart = new Chart(
        document.getElementById('userCategoriesChart'),
        config
      );

};

const GraphUserSurveys = function (result) {

    let labels = []
	let surveysData = []
	
    result.labels.forEach(element => {
            labels.push(element)
    });

    result.user_score.forEach(element => {
            surveysData.push(parseFloat(element))
    });

    const data = {
        labels: labels,
        datasets: [{
            label: 'My First dataset',
            backgroundColor: 'rgba(255, 193, 7)',
            borderColor: 'rgb(255, 193, 7)',
            data: surveysData,
        }]
    };

    const config = {
        type: 'bar',
        data: data,
        options: {}
    };

    const userSurveysChart = new Chart(
        document.getElementById('userSurveysChart'),
        config
      );

};

const ResultCategoryUSer = function () {
	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/categories/score',
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
			GraphUserCategories(response);
		}
	});
}

const ResultSurveyUSer = function () {
	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/surveys/score',
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
			GraphUserSurveys(response);
		}
	});
}

window.onload = function () {
	ResultCategoryUSer();
	ResultSurveyUSer();

}
