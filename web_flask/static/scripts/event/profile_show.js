$(document).ready(function () {
	var url = window.location.pathname;
	var url_splitted = url.split('/')

	if (url_splitted[1] == 'profiles' && url_splitted[3] == 'show') {
		var profile_id = url_splitted[2];

		$.ajaxSetup({
			headers: {
				'Authorization': `Bearer ${localStorage.getItem('token')}`
			}
		});

		$.get('http://0.0.0.0:5002/api/v1/profiles/' + profile_id, function (data) {
      btn_delete = profileDeleteButton(data);
      btn_edit = profileEditButton(data);
      bts = $('<div class="btn-group float-right profile"></div>').append(btn_edit).append(btn_delete);
			$('body > .container-fluid > h1').text(data.first_name + ' ' + data.last_name).append(bts);
      btnProfileEditEvent();
      btnProfileDeleteEvent();
		});
	}
});
