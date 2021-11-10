const getMe = function () {
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/me',
    type: 'GET',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },

    error: function (data) {
      dataResponse = data.responseJSON;
      statusCode = data.status;

      switch (statusCode) {
        case 498:
          localStorage.removeItem('token');
          window.location = '/';
          break;
      }
    },
    success: function (response) {
      if (response.user.roles[0] === 'ROLE_ADMIN') {
        $('.navbar-nav').append(GenerateMenu());
      }
    }
  }
  );
};

function GenerateMenu () {
  return (`<li class="nav-item dropdown active">
	<a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button"
		data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
		Profiles
	</a>
	<div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
		<a class="dropdown-item" href="/profiles">List Profiles</a>
		<a class="dropdown-item" href="/profiles/create">Create Profile</a>
	</div>
</li>

<li class="nav-item dropdown active">
	<a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button"
		data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
		Surveys
	</a>
	<div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
		<a class="dropdown-item" href="/surveys">List Surveys</a>
		<a class="dropdown-item" href="/surveys/create">Create Survey</a>
	</div>
</li>


<li class="nav-item dropdown active">
	<a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button"
		data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
		Questions
	</a>
	<div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
		<a class="dropdown-item" href="/questions">List Questions</a>
		<a class="dropdown-item" href="/questions/create">Create Question</a>
	</div>
</li>

<li class="nav-item dropdown active">
	<a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button"
		data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
		Categories
	</a>
	<div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
		<a class="dropdown-item" href="/categories">List Categories</a>
		<a class="dropdown-item" href="/categories/create">Create Category</a>
	</div>
</li>

<li class="nav-item dropdown active">
	<a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button"
		data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
		Users
	</a>
	<div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
		<a class="dropdown-item" href="/users">List Users</a>
		<a class="dropdown-item" href="/users/create">Create User</a>
	</div>
</li>

<li class="nav-item dropdown active">
	<a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button"
		data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
		Proposals
	</a>
	<div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
		<a class="dropdown-item" href="/proposals">List Proposals</a>
		<a class="dropdown-item" href="/proposals/create">Create Proposal</a>
	</div>
</li>
`);
}

$(document).ready(function () {
  if (localStorage.getItem('token')) {
    getMe();
  }
});
