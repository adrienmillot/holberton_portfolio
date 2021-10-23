const getProfile = function () {
	$.ajax({
		url: 'https://ss-api.2835holberton.tech/api/v1/profiles',
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
			response.results.forEach(element => {
				const htmlContent = articleHtml(element);
				$(htmlContent).appendTo('.infos');
				
			});

		}
	});
}

function articleHtml(element) {
	return (`
	  <article>
	  <h2>Profile</h2>
	  <h3>Hello ${element.first_name} !</h3>	
	  <div id='info'>
    <ul>
	  <li>First name:${element.first_name}</li> 
	  <li>Last name: ${element.last_name}</li>
	  <li>Member since ${element.created_at}</li>
    </ul>
	  </div>  
	  </article>`)
}



$(() => {
	getProfile();
	});
