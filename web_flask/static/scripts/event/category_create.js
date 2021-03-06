
const createCategory = function (name) {
  const obj = { name: name };
  const json_data = JSON.stringify(obj);
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/categories',
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
      const name = response.name;
      $('section.alert_success_create_category').empty();

      $('section.alert_success_create_category').append(MessageAlertCategoryCreate(name));
    }
  }
  );
};

function MessageAlertCategoryCreate (name) {
  return (`
<div class="alert alert-success" role="alert">
  Your category ${name}, have been succefuly created
</div>`);
}

$(() => {
  $('#btn_create_category').on('click', () => {
    const name = $('#txt_category_name').val().trim();
    const secure_name = name.replace(/</g, '&lt;').replace(/>/g, '&gt;');

    createCategory(secure_name);
  });
});
