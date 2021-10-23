$(document).ready(function () {
	var url = window.location.pathname;
	var url_splitted = url.split('/')

	if (url_splitted[1] == 'categories' && url_splitted[3] == 'show') {
		var category_id = url_splitted[2];

		$.ajaxSetup({
			headers: {
				'Authorization': `Bearer ${localStorage.getItem('token')}`
			}
		});

		$.get('https://ss-api.2835holberton.tech/api/v1/categories/' + category_id, function (data) {
      btn_delete = categoryDeleteButton(data);
      btn_edit = categoryEditButton(data);
      bts = $('<div class="btn-group float-right category"></div>').append(btn_edit).append(btn_delete);
			$('body > .container-fluid > h1').text(data.name).append(bts);
      btncategoryEditEvent();
      btncategoryDeleteEvent();
		});
	}
});
