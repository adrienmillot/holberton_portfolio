
const editCategory = function (name, category_id) {
    const obj = { name: name };
    const json_data = JSON.stringify(obj);
  
    $.ajax({
      url: 'http://0.0.0.0:5002/api/v1/categories/' + category_id,
      type: 'PUT',
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
      data: json_data,
      contentType: 'application/json',
  
      success: function (response) {
        $('section.alert_success_edit_category').empty();
  
        $('section.alert_success_edit_category').append(getAlertUpdateElement('Your category <strong>' + response.name + '</strong> has been well updated'));
      }
    }
    );
  };
  
  function getAlertUpdateElement (message) {
    return $('<div class="alert alert-success" role="alert"></div>').html(message);
  }
  
  const setCategoryName = function (category_id) {
    $.ajax({
      url: 'http://0.0.0.0:5002/api/v1/categories/' + category_id,
      type: 'GET',
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
      contentType: 'application/json',
  
      success: function (response) {
        $('#txt_category_name').val(response.name);
      }
    });
  };
  
  $(document).ready(function () {
    const url = window.location.pathname;
    const url_args = url.split('/');
    if (url_args[1] == 'categories' && url_args[3] == 'edit') {
          const category_id = url_args[2];
  
          setCategoryName(category_id);
    
    $('#btn_edit_category').click(function () {
      const name = $('#txt_category_name').val().trim();
      editCategory(name, category_id);
    });
  }
  });
  