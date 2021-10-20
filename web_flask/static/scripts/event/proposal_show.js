$(document).ready(function () {
	var url = window.location.pathname;
	var url_splitted = url.split('/')

	if (url_splitted[1] == 'proposals' && url_splitted[3] == 'show') {
		var proposal_id = url_splitted[2];

		$.ajaxSetup({
			headers: {
				'Authorization': `Bearer ${localStorage.getItem('token')}`
			}
		});

		$.get('http://0.0.0.0:5002/api/v1/proposals/' + proposal_id, function (data) {
			$('body > .container-fluid > h1').text(data.label)
		});
	}
});
