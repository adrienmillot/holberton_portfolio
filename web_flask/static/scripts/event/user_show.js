$(document).ready(function () {
	var url = window.location.pathname;
	var url_splitted = url.split('/')

	if (url_splitted[1] == 'users' && url_splitted[3] == 'show') {
		var user_id = url_splitted[2];

		$.ajaxSetup({
			headers: {
				'Authorization': `Bearer ${localStorage.getItem('token')}`
			}
		});

		$.get('http://0.0.0.0:5002/api/v1/users/' + user_id, function (data) {
      btn_delete = userDeleteButton(data);
      btn_edit = userEditButton(data);
      bts = $('<div class="btn-group float-right user"></div>').append(btn_edit).append(btn_delete);
			$('body > .container-fluid > h1').text(data.username).append(bts);
      btnUserEditEvent();
      btnUserDeleteEvent();
		});
	}
});
