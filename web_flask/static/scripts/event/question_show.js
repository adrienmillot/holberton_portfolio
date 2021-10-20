$(document).ready(function () {
	var url = window.location.pathname;
	var url_splitted = url.split('/');

	if (url_splitted[1] == 'questions' && url_splitted[3] == 'show') {
		var question_id = url_splitted[2];
		$.ajaxSetup({
			headers: {
				'Authorization': `Bearer ${localStorage.getItem('token')}`
			}
		});

		$.get('http://0.0.0.0:5002/api/v1/questions/' + question_id, function (data) {
      btn_delete = questionDeleteButton(data);
      btn_edit = questionEditButton(data);
      bts = $('<div class="btn-group float-right question"></div>').append(btn_edit).append(btn_delete);
			$('body > .container-fluid > h1').text(data.label).append(bts);
      btnQuestionEditEvent();
      btnQuestionDeleteEvent();

      $labels = $('<div id="labels"></div>');
      $('body > .container-fluid').append($labels);

      $.get('http://0.0.0.0:5002/api/v1/categories/' + data.category_id, function (data) {
        $label = $('<span></span>').attr('class', 'badge badge-secondary mr-1').text(data.name)
        $labels.append($label)
      });

      $.get('http://0.0.0.0:5002/api/v1/surveys/' + data.survey_id, function (data) {
        $label = $('<span></span>').attr('class', 'badge badge-info').text(data.name)
        $labels.append($label)
      });
		});
	}
});
