const GraphCategoryQuestions = function (result) {
  const labels = [];
  const categoryQuestionsData = [];

  result.category.labels.forEach(element => {
    labels.push(element);
  });

  result.category.user_scores.forEach(element => {
    categoryQuestionsData.push(parseFloat(element));
  });

  const data = {
    labels: labels,
    datasets: [{
      label: 'Category Questions dataset',
      backgroundColor: 'rgba(255, 193, 7)',
      borderColor: 'rgb(255, 193, 7)',
      data: categoryQuestionsData
    }]
  };

  const config = {
    type: 'bar',
    data: data,
    options: {}
  };

  const ScoreCategoryQuestionChart = new Chart(
    document.getElementById('ScoreCategoryQuestionChart'),
    config
  );
};

const ResultCategory = function (category_id) {
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/categories/' + category_id + '/score',
    type: 'GET',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    error: function (data) {
      dataResponse = data.responseJSON;
      statusCode = data.status;
      switch (statusCode) {
        case 498:
          localStorage.removeItem('token');
          window.location = '/';
          break;
      }
    },
    success: function (response) {
      const htmlContent = CategoryScore(response.message);
      $(htmlContent).appendTo('.infos_Category_Score');
    }
  });
};

const CategoryScore = function (score) {
  return (`
	<article>
	<h3>${score}</h3>
	</article>
	`);
};

const ResultCategoryQuestions = function (category_id) {
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/categories/' + category_id + '/question_score',
    type: 'GET',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    error: function (data) {
      dataResponse = data.responseJSON;
      statusCode = data.status;
      switch (statusCode) {
        case 498:
          localStorage.removeItem('token');
          window.location = '/';
          break;
      }
    },
    success: function (response) {
      GraphCategoryQuestions(response);
    }
  });
};

window.onload = function () {
  const url = window.location.pathname;
  const url_splitted = url.split('/');

  if (url_splitted[1] == 'categories' && url_splitted[3] == 'show') {
    const category_id = url_splitted[2];

    ResultCategory(category_id);

    ResultCategoryQuestions(category_id);
  }
};
