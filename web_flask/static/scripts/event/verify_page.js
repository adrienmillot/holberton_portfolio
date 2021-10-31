const verify_page = function (page) {
	let location = {entrypoint: page};
	let json_location = JSON.stringify(location);

	$.ajax({
		url: 'http://0.0.0.0:5002/api/v1/auth/verify_page',
		type: 'GET',
		headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` },
		data: location,
		error: function (data, textStatus, request) {
			dataResponse = data.responseJSON;
			statusCode = data.status;


			switch (statusCode) {
				case 498:
					localStorage.removeItem('token');
					window.location = "/";
					break;
				case 400:
					if (dataResponse.message == 'You have not right to display this page.') {
						window.location = '/dashboard';
					}
					break;
			}
		},
		success: function (response) {
			console.log(response);	
		}
	});
}

document.onreadystatechange = function(e)
{
	if (document.readyState != 'complete') {
		const current_page =  window.location.href;
		const url_args = current_page.split('/');
		let location = "/" +  url_args[3];

		if (url_args[6] && url_args[6] == 'answer') {
			location = '/answers';
		}

		console.log(location);
		verify_page(location);
	}
};



// $(document).ready(function () {
// 	const current_page =  window.location.href;
// 	const url_args = current_page.split('/');
// 	const location = "/" +  url_args[3];
// 	if (url_args[6] === 'answer') {
// 		location
// 	}
// 	console.log(location);
// 	verify_page(location);
// });