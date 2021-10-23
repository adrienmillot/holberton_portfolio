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

		$.get('https://ss-api.2835holberton.tech/api/v1/proposals/' + proposal_id, function (data) {
      btn_delete = proposalDeleteButton(data);
      btn_edit = proposalEditButton(data);
      bts = $('<div class="btn-group float-right proposal"></div>').append(btn_edit).append(btn_delete);
			$('body > .container-fluid > h1').text(data.label).append(bts);
      btnProposalEditEvent();
      btnProposalDeleteEvent();
		});
	}
});
