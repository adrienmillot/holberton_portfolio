const createProfile = function (first_name, last_name, gender) {
  // let born_at = ""
  const obj = { first_name: first_name, last_name: last_name, gender: gender };
  const json_data = JSON.stringify(obj);
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/profiles',
    type: 'POST',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    data: json_data,
    contentType: 'application/json',
    error: function (data) {
      dataResponse = data.responseJSON;
      statusCode = data.status;

      switch (statusCode) {
        case 401:
          console.error(dataResponse.message);
          break;
      }
    },
    success: function (response) {
      const FirstName = response.first_name;
      $('section.alert_success_create_profile').empty();
      $('section.alert_success_create_profile').append(MessageProfileSuccessCreate(FirstName));
    }
  }
  );
};

function MessageProfileSuccessCreate (FirstName) {
  return (`
<div class="alert alert-success" role="alert">
  Your profile for <strong>${FirstName}</strong>, have been succefuly created
</div>`);
}

$(document).ready(function () {
  $('#btn_create_profile').on('click', () => {
    const first_name = $('#txt_profile_first_name').val().trim();
    const last_name = $('#txt_profile_last_name').val().trim();
    const gender = $('#select_gender_for_profile').val();
    const secure_fname = first_name.replace(/</g, '&lt;').replace(/>/g, '&gt;');
    const secure_lname = last_name.replace(/</g, '&lt;').replace(/>/g, '&gt;');

    createProfile(secure_fname, secure_lname, gender);
  });
});
