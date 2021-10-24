$(document).ready(function () {
	const url = window.location.pathname;
	const url_args = url.split('/');
	if (url_args[1] == 'surveys' && url_args[4] == 'answer') {
		  const survey_id = url_args[2];
		  const survey_name = url_args[2];
	}})