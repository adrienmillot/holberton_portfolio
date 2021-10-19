/**
 * get request to api to get all users
 */

 const getUsersList = function () {

	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/users',
		type:'GET',
		headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` },
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
			console.log(response)
			userList(response.results);
		}
	});
}

/**
 * Generate DOM for show button.
 */
function userShowButton(user) {
	return $('<button class="btn show btn-secondary btn-sm"></button>').attr('data-id', user.id).html(`
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
function userEditButton(user) {
	return $('<button class="btn edit btn-secondary btn-sm"></button>').attr('data-id', user.id).html(`<svg xmlns="http://www.w3.org/2000/svg"
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
function userDeleteButton(user) {
	return $('<button class="btn delete btn-secondary btn-sm"></button>').attr('data-id', user.id).html(`<svg xmlns="http://www.w3.org/2000/svg"
	width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
	<path
		d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z" />
</svg>`);
}

/**
 * Generate DOM for action buttons.
 */
function userActionsButton(user) {
	var showUserButton = userShowButton(user);
	var editUserButton = userEditButton(user);
	var deleteUserButton = userDeleteButton(user);

	return $('<div class="btn-group" role="group"></div>').append(showUserButton).append(editUserButton).append(deleteUserButton);
}

/**
 * Generate DOM for user row.
 */
function userRow(user, count) {
	var countTh = $('<th></th>').text('#' + count);
	var nameTd = $('<td></td>').text(user.username);
	var idTd = $('<td></td>').text(user.id);
	var emptyTd = $('<td></td>')
	var btnActionTd = $('<td></td>').append(userActionsButton(user));

	return $('<tr class="user"></tr>').append(countTh).append(nameTd).append(idTd).append(emptyTd).append(btnActionTd);
}

/**
 * 
 */
function userList(users) {
	$.each(users, function (key, user) {
		$('tbody.users_list').append(userRow(user, key));
	});

	btnUserShowEvent();
	btnUserEditEvent();
	btnUserDeleteEvent();
}

function btnUserShowEvent() {
	/**
	 * Click on show button
	 */
	$('.user .btn.show').click(function () {
		id = $(this).attr('data-id');
		localStorage.setItem('show_user_id', id)
		window.location = '/user_show'

		
	});

}

function btnUserEditEvent() {
	/**
	 * Click on edit button
	 */
	$('.user .btn.edit').click(function () {
		id = $(this).attr('data-id');
		localStorage.setItem('edit_user_id', id)
		window.location = '/user_edit'
	});

}

function btnUserDeleteEvent() {
	/**
	 * Click on delete button
	 */
	$('.user .btn.delete').click(function () {
		id = $(this).attr('data-id');
		delet = deleteAction(id);
		if (delet = true){
			$(this).parent().parent().parent().remove()
	}
})
};


function deleteAction(id) {

	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/users/' + id,
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
				$('section.alert_success_delete_user').append(MessageConfirmation())
				return (true)
			})
		}
	})
}





function MessageConfirmation() {
	return (`
	<div class="alert alert-success" role="alert">
	  You're user, have been succefuly deleted
	</div>`)
}


$(document).ready(function () {
	getUsersList();
});
