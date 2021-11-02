
const editProposal = function (label, proposal_id) {
  const obj = { label: label };
  const json_data = JSON.stringify(obj);

  $.ajax({
	  url: 'http://0.0.0.0:5002/api/v1/proposals/' + proposal_id,
	  type: 'PUT',
	  headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
	  data: json_data,
	  contentType: 'application/json',

	  success: function (response) {
      $('section.alert_success_edit_proposal').empty();

      $('section.alert_success_edit_proposal').append(getAlertUpdateElement('Your proposal <strong>' + response.label + '</strong> has been well updated'));
	  }
  }
  );
};

const setProposalLabel = function (proposal_id) {
  $.ajax({
	  url: 'http://0.0.0.0:5002/api/v1/proposals/' + proposal_id,
	  type: 'GET',
	  headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
	  contentType: 'application/json',

	  success: function (response) {
      $('#txt_proposal_label').val(response.label);
	  }
  });
};

$(document).ready(function () {
  const url = window.location.pathname;
  const url_args = url.split('/');
  if (url_args[1] == 'proposals' && url_args[3] == 'edit') {
		  const proposal_id = url_args[2];

		  setProposalLabel(proposal_id);

    $('#btn_edit_proposal').click(function () {
	  const label = $('#txt_proposal_label').val().trim();
	  const secure_label = label.replace(/</g, '&lt;').replace(/>/g, '&gt;');

	  editProposal(secure_label, proposal_id);
    });
  }
});
