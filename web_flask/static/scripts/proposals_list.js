/**
 * get request to api to get all proposals
 */

const getProposalsListPage = function (page) {
	let limit = 10
	let obj = { limit: limit, page: page }

	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/proposals',
		type: 'GET',
		headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` },
		data: obj,
		error: function (data) {
			dataResponse = data.responseJSON
			statusCode = data.status

			switch (statusCode) {
				case 498:
					// Remove auth_token
					localStorage.removeItem('token');
					// Redirect to homepage
					window.location = "/";
					break;
			}
		},
		success: function (response) {
			proposalList(response.results);
			if (response.page_count > 1) {
				buildPaginationBtnsProposal(response.page_count, parseInt(page))
			}
		}
	});
}
/** 
 * Generate precedent link
 * Generate i times pagination links
 * Generate next link
 */
function buildPaginationBtnsProposal(page_count, page) {
	if (page === 1 || page === undefined) {
		var previousBtnDisable = 'disabled'
	} else {
		var previousBtnDisable = ''
	}
	if (page === page_count) {
		var nextBtnDisable = 'disabled'
	} else {
		var nextBtnDisable = ''
	}

	$('ul#proposal_pagination').append('<li class="page-item ' + previousBtnDisable + '"><a class="page-link" id="prevBtnProposal" tabindex="-1" aria-disabled="true">Previous</a></li>')

	for (i = 1; i <= page_count; i++) {
		$('ul#proposal_pagination').append($(' <li class="page-item"></li>').append(NavigationBtnProposal(i)))
		var linkAction = $('a#' + i + '_proposal.page-link')
		linkAction.click(function () {
			new_page = $(this).attr('data-id')
			window.location = '/proposals?page=' + new_page
		})
	}
	$('ul#proposal_pagination').append('<li class="page-item ' + nextBtnDisable + '"><a class="page-link" id="nextBtnProposal">Next</a></li>')
	$('a#prevBtnProposal.page-link').click(function () {
		if (page !== 1) {
			window.location = '/proposals?page=' + (page - 1)
		}
	});
	$('a#nextBtnProposal.page-link').click(function () {
		if (page !== page_count) {
			window.location = '/proposals?page=' + (page + 1)
		}
	})
}


function NavigationBtnProposal(i) {
	return $('<a class="page-link" id="' + i + '_proposal">' + i + '</a>').attr('data-id', i)
}


/**
 * Generate DOM for show button.
 */
function proposalShowButton(proposal) {
	return $('<button class="btn show btn-secondary btn-sm"></button>').attr('data-id', proposal.id).html(`
	<svg xmlns="http://www.w3.org/2000/svg"
		width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16">
		<path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z" />
		<path
			d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8zm8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z" />
	</svg>`);
}

/**
 * Generate DOM for edit button.
 */
function proposalEditButton(proposal) {
	return $('<button class="btn edit btn-secondary btn-sm"></button>').attr('data-id', proposal.id).html(`<svg xmlns="http://www.w3.org/2000/svg"
	width="16" height="16" fill="currentColor" class="bi bi-pencil-square"
	viewBox="0 0 16 16">
	<path
		d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z" />
	<path fill-rule="evenodd"
		d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z" />
</svg>`);
}


/**
 * Generate DOM for delete button.
 */
function proposalDeleteButton(proposal) {
	return $('<button class="btn delete btn-secondary btn-sm"></button>').attr('data-id', proposal.id).html(`<svg xmlns="http://www.w3.org/2000/svg"
	width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
	<path
		d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z" />
</svg>`);
}

/**
 * Generate DOM for action buttons.
 */
function proposalActionsButton(proposal) {
	var showProposalButton = proposalShowButton(proposal);
	var editProposalButton = proposalEditButton(proposal);
	var deleteProposalButton = proposalDeleteButton(proposal);

	return $('<div class="btn-group" role="group"></div>').append(showProposalButton).append(editProposalButton).append(deleteProposalButton);
}

/**
 * Generate DOM for proposal row.
 */
function proposalRow(proposal, count) {
	var countTh = $('<th></th>').text('#' + count);
	var nameTd = $('<td></td>').text(proposal.label);
	var idTd = $('<td></td>').text(proposal.id);
	var emptyTd = $('<td></td>')
	var btnActionTd = $('<td></td>').append(proposalActionsButton(proposal));

	return $('<tr class="proposal"></tr>').append(countTh).append(nameTd).append(idTd).append(emptyTd).append(btnActionTd);
}

/**
 * 
 */
function proposalList(proposals) {
	$.each(proposals, function (key, proposal) {
		$('tbody.proposals_list').append(proposalRow(proposal, key));
	});

	btnProposalShowEvent();
	btnProposalEditEvent();
	btnProposalDeleteEvent();
}

function btnProposalShowEvent() {
	/**
	 * Click on show button
	 */
	$('.proposal .btn.show').click(function () {
		proposal_id = $(this).attr('data-id');
		window.location = '/proposals/' + proposal_id + '/show'


	});

}

function btnProposalEditEvent() {
	/**
	 * Click on edit button
	 */
	$('.proposal .btn.edit').click(function () {
		proposal_id = $(this).attr('data-id');
		window.location = '/proposals/' + proposal_id + '/edit'
	});

}

function btnProposalDeleteEvent() {
	/**
	 * Click on delete button
	 */
	$('.proposal .btn.delete').click(function () {
		proposal_id = $(this).attr('data-id');
		delet = deleteActionProposal(proposal_id);
		if (delet = true) {
			$(this).parent().parent().parent().remove()
		}
	})
};


function deleteActionProposal(id) {

	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/proposals/' + id,
		type: 'DELETE',
		headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` },
		error: function (data) {
			dataResponse = data.responseJSON
			statusCode = data.status

			switch (statusCode) {
				case !200:
					console.error(dataResponse.message);
					break;
			}
		},
		success: function (data) {
			$(document).ready(function () {
				$('section.alert_success_delete_proposal').empty();
				$('section.alert_success_delete_proposal').append(MessageConfirmationDeleteProposal())
				return (true)
			})
		}
	})
}

function MessageConfirmationDeleteProposal() {
	return (`
	<div class="alert alert-success" role="alert">
	  Your proposal, have been succefuly deleted
	</div>`)
}

$(document).ready(function () {
	var page = $('#page_argument_proposal').val()
	getProposalsListPage(page);
});
