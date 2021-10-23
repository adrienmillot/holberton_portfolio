/**
 * get request to api to get all categorys
 */

 const getCategoriesListPage = function () {

	$.ajax({
		url: 'http://ss-api.2835holberton.tech/api/v1/categories',
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
			categoryListForCategory(response.results);
		}
	});
}

/**
 * Generate DOM for show button.
 */
function categoryShowButton(category) {
	return $('<button class="btn show btn-secondary btn-sm"></button>').attr('data-id', category.id).html(`
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
function categoryEditButton(category) {
	return $('<button class="btn edit btn-secondary btn-sm"></button>').attr('data-id', category.id).html(`<svg xmlns="http://www.w3.org/2000/svg"
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
function categoryDeleteButton(category) {
	return $('<button class="btn delete btn-secondary btn-sm"></button>').attr('data-id', category.id).html(`<svg xmlns="http://www.w3.org/2000/svg"
	width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
	<path
		d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z" />
</svg>`);
}

/**
 * Generate DOM for action buttons.
 */
function categoryActionsButton(category) {
	var showcategoryButton = categoryShowButton(category);
	var editcategoryButton = categoryEditButton(category);
	var deletecategoryButton = categoryDeleteButton(category);

	return $('<div class="btn-group" role="group"></div>').append(showcategoryButton).append(editcategoryButton).append(deletecategoryButton);
}

/**
 * Generate DOM for category row.
 */
function categoryRow(category, count) {
	var countTh = $('<th></th>').text('#' + count);
	var nameTd = $('<td></td>').text(category.name);
	var idTd = $('<td></td>').text(category.id);
	var emptyTd = $('<td></td>')
	var btnActionTd = $('<td></td>').append(categoryActionsButton(category));

	return $('<tr class="category"></tr>').append(countTh).append(nameTd).append(idTd).append(emptyTd).append(btnActionTd);
}

/**
 * 
 */
function categoryListForCategory(categorys) {
	$.each(categorys, function (key, category) {
		$('tbody.categories_list').append(categoryRow(category, key));
	});

	btncategoryShowEvent();
	btncategoryEditEvent();
	btncategoryDeleteEvent();
}

function btncategoryShowEvent() {
	/**
	 * Click on show button
	 */
	$('.category .btn.show').click(function () {
		category_id = $(this).attr('data-id');
		window.location = '/categories/' + category_id + '/show'

		
	});

}

function btncategoryEditEvent() {
	/**
	 * Click on edit button
	 */
	$('.category .btn.edit').click(function () {
		category_id = $(this).attr('data-id');
		window.location = '/categories/' + category_id + '/edit'
	});

}

function btncategoryDeleteEvent() {
	/**
	 * Click on delete button
	 */
	$('.category .btn.delete').click(function () {
		id = $(this).attr('data-id');
		delet = deleteActionCategory(id);
		if (delet = true){
			$(this).parent().parent().parent().remove()
	}
})
};


function deleteActionCategory(id) {

	$.ajax({
		url: 'http://ss-api.2835holberton.tech/api/v1/categories/' + id,
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
				$('section.alert_success_delete_category').empty();
				$('section.alert_success_delete_category').append(MessageConfirmationDeleteCategory())
				return (true)
			})
		}
	})
}





function MessageConfirmationDeleteCategory() {
	return (`
	<div class="alert alert-success" role="alert">
	  Your category, have been succefuly deleted
	</div>`)
}


$(document).ready(function () {
	getCategoriesListPage();
});
