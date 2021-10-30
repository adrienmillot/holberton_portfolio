const verify_page = function () {
	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/auth/verify_page',
		type: 'GET',
		headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` },

		error: function (data) {
			dataResponse = data.responseJSON
			statusCode = data.status


			switch (statusCode) {
				case 498:
					localStorage.removeItem('token')
					window.location = "/"
					break;
			}
		},
		success: function (response) {
			
				}


			});

		}

$(document).ready(function () {
	var current_page =  window.location.href;
	console.log(current_page)
	verify_page(current_page);
	});