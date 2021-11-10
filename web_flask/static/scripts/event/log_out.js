$(document).ready(function () {
  token = localStorage.getItem('token');

  if (!token) {
    $('#user_btn').hide();
    $('#secure_menu').hide();
  }
});

const redirectToIndex = function () {
  localStorage.removeItem('token');
  window.location = '/';
};

$(() => {
  $('#btn_logout').on('click', () => {
    redirectToIndex();
  });
});
