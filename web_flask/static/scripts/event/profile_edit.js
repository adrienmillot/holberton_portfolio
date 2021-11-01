
const editProfile = function (first_name, last_name, gender , profile_id) {
	const obj = { first_name: first_name, last_name: last_name, gender: gender };
	const json_data = JSON.stringify(obj);
  
	$.ajax({
	  url: 'http://0.0.0.0:5002/api/v1/profiles/' + profile_id,
	  type: 'PUT',
	  headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
	  data: json_data,
	  contentType: 'application/json',
  
	  success: function (response) {
		$('section.alert_success_edit_profile').empty();
  
		$('section.alert_success_edit_profile').append(getAlertUpdateElement('Your profile for <strong>' + response.first_name + " " + response.last_name + '</strong> has been well updated'));
	  }
	}
	);
  };
  
  
  const setProfileFirstName = function (profile_id) {
	$.ajax({
	  url: 'http://0.0.0.0:5002/api/v1/profiles/' + profile_id,
	  type: 'GET',
	  headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
	  contentType: 'application/json',
  
	  success: function (response) {
		$('#txt_profile_edit_first_name').val(response.first_name);
	  }
	});
  };

  const setProfileLastName = function (profile_id) {
	$.ajax({
	  url: 'http://0.0.0.0:5002/api/v1/profiles/' + profile_id,
	  type: 'GET',
	  headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
	  contentType: 'application/json',
  
	  success: function (response) {
		$('#txt_profile_edit_last_name').val(response.last_name);
	  }
	});
  };

  const setProfileGender = function (profile_id) {
	$.ajax({
	  url: 'http://0.0.0.0:5002/api/v1/profiles/' + profile_id,
	  type: 'GET',
	  headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
	  contentType: 'application/json',
  
	  success: function (response) {
		$('#select_gender_for_profile_update').val(response.gender);
	  }
	});
  };
  
  $(document).ready(function () {
	const url = window.location.pathname;
	const url_args = url.split('/');
	if (url_args[1] == 'profiles' && url_args[3] == 'edit') {
		  const profile_id = url_args[2];
  
		  setProfileFirstName(profile_id);
		  setProfileLastName(profile_id);
		  setProfileGender(profile_id);
	
	$('#btn_edit_profile').click(function () {
	  const first_name = $('#txt_profile_edit_first_name').val().trim();
	  const last_name = $('#txt_profile_edit_last_name').val().trim();
	  const gender = $('#select_gender_for_profile_update').val();
	  let secure_fname = first_name.replace(/</g, "&lt;").replace(/>/g, "&gt;");
	  let secure_lname = last_name.replace(/</g, "&lt;").replace(/>/g, "&gt;");

	  editProfile(secure_fname, secure_lname, gender, profile_id);
	});
  }
  });
  