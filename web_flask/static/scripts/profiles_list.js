/**
 * get request to api to get all Profiles
 */

const getProfilesListPage = function (page) {
  const limit = 10;
  const obj = { limit: limit, page: page };

  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/profiles',
    type: 'GET',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    data: obj,
    error: function (data) {
      dataResponse = data.responseJSON;
      statusCode = data.status;

      switch (statusCode) {
        case 498:
          // Remove auth_token
          localStorage.removeItem('token');
          // Redirect to homepage
          window.location = '/';
          break;
      }
    },
    success: function (response) {
      profileList(response.results);
      if (response.page_count > 1) {
        buildPaginationBtnsProfile(response.page_count, parseInt(page));
      }
    }
  });
};
/**
 * Generate precedent link
 * Generate i times pagination links
 * Generate next link
 */
function buildPaginationBtnsProfile (page_count, page) {
  if (page === 1 || page === undefined) {
    var previousBtnDisable = 'disabled';
  } else {
    var previousBtnDisable = '';
  }
  if (page === page_count) {
    var nextBtnDisable = 'disabled';
  } else {
    var nextBtnDisable = '';
  }

  $('ul#profile_pagination').append('<li class="page-item ' + previousBtnDisable + '"><a class="page-link" id="prevBtnProfile" tabindex="-1" aria-disabled="true">Previous</a></li>');

  for (i = 1; i <= page_count; i++) {
    $('ul#profile_pagination').append($(' <li class="page-item"></li>').append(NavigationBtnProfile(i)));
    const linkAction = $('a#' + i + '_profile.page-link');
    linkAction.click(function () {
      new_page = $(this).attr('data-id');
      window.location = '/profiles?page=' + new_page;
    });
  }
  $('ul#profile_pagination').append('<li class="page-item ' + nextBtnDisable + '"><a class="page-link" id="nextBtnProfile">Next</a></li>');
  $('a#prevBtnProfile.page-link').click(function () {
    if (page !== 1) {
      window.location = '/profiles?page=' + (page - 1);
    }
  });
  $('a#nextBtnProfile.page-link').click(function () {
    if (page !== page_count) {
      window.location = '/profiles?page=' + (page + 1);
    }
  });
}

function NavigationBtnProfile (i) {
  return $('<a class="page-link" id="' + i + '_profile">' + i + '</a>').attr('data-id', i);
}

/**
 * Generate DOM for show button.
 */
function profileShowButton (profile) {
  return $('<button class="btn show btn-secondary btn-sm"></button>').attr('data-id', profile.id).html(`
	<svg xmlns="http://www.w3.org/2000/svg"
		width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16">
		<path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z" />
		<path
			d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8zm8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z" />
	</svg>`);
}

/**
 * Generate DOM for edit button.
 */
function profileEditButton (profile) {
  return $('<button class="btn edit btn-secondary btn-sm"></button>').attr('data-id', profile.id).html(`<svg xmlns="http://www.w3.org/2000/svg"
	width="16" height="16" fill="currentColor" class="bi bi-pencil-square"
	viewBox="0 0 16 16">
	<path
		d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z" />
	<path fill-rule="evenodd"
		d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z" />
</svg>`);
}

/**
 * Generate DOM for delete button.
 */
function profileDeleteButton (profile) {
  return $('<button class="btn delete btn-secondary btn-sm"></button>').attr('data-id', profile.id).html(`<svg xmlns="http://www.w3.org/2000/svg"
	width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
	<path
		d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z" />
</svg>`);
}

/**
 * Generate DOM for action buttons.
 */
function profileActionsButton (profile) {
  const showProfileButton = profileShowButton(profile);
  const editProfileButton = profileEditButton(profile);
  const deleteProfileButton = profileDeleteButton(profile);

  return $('<div class="btn-group" role="group"></div>').append(showProfileButton).append(editProfileButton).append(deleteProfileButton);
}

/**
 * Generate DOM for profile row.
 */
function profileRow (profile, count) {
  const countTh = $('<th></th>').text('#' + count);
  const nameTd = $('<td></td>').text(profile.first_name);
  const idTd = $('<td></td>').text(profile.last_name);
  const genderTd = $('<td></td>').text(profile.gender);
  const btnActionTd = $('<td></td>').append(profileActionsButton(profile));

  return $('<tr class="profile"></tr>').append(countTh).append(nameTd).append(idTd).append(genderTd).append(btnActionTd);
}

/**
 *
 */
function profileList (profiles) {
  $.each(profiles, function (key, profile) {
    $('tbody.profiles_list').append(profileRow(profile, key));
  });

  btnProfileShowEvent();
  btnProfileEditEvent();
  btnProfileDeleteEvent();
}

function btnProfileShowEvent () {
  /**
   * Click on show button
   */
  $('.profile .btn.show').click(function () {
    profile_id = $(this).attr('data-id');
    window.location = '/profiles/' + profile_id + '/show';
  });
}

function btnProfileEditEvent () {
  /**
   * Click on edit button
   */
  $('.profile .btn.edit').click(function () {
    profile_id = $(this).attr('data-id');
    window.location = '/profiles/' + profile_id + '/edit';
  });
}

function btnProfileDeleteEvent () {
  /**
	 * Click on delete button
	 */
  $('.profile .btn.delete').click(function () {
    profile_id = $(this).attr('data-id');
    delet = deleteActionProfile(profile_id);
    if (delet = true) {
      $(this).parent().parent().parent().remove();
    }
  });
}

function deleteActionProfile (id) {
  $.ajax({
    url: 'http://0.0.0.0:5002/api/v1/profiles/' + id,
    type: 'DELETE',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
    error: function (data) {
      dataResponse = data.responseJSON;
      statusCode = data.status;

      switch (statusCode) {
        case !200:
          console.error(dataResponse.message);
          break;
      }
    },
    success: function (data) {
      $(document).ready(function () {
        $('section.alert_success_delete_profile').empty();
        $('section.alert_success_delete_profile').append(MessageConfirmationDeleteProfile());
        return (true);
      });
    }
  });
}

function MessageConfirmationDeleteProfile () {
  return (`
	<div class="alert alert-success" role="alert">
	  Your profile, have been succefuly deleted
	</div>`);
}

$(document).ready(function () {
  const page = $('#page_argument_profile').val();
  getProfilesListPage(page);
});
