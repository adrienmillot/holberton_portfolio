$(document).ready(function () {
  token = localStorage.getItem('token');

  if (token) {
    $('#btn_login').hide();
  }
  if ((!token) && (window.pathname != '/') && (window.pathname != '/login')) {
    window.pathname = '/';
  }
});

const redirectToLogin = function () {
  window.location = '/login';
};

$(() => {
  $('#btn_login').on('click', () => {
    redirectToLogin();
  });
});
