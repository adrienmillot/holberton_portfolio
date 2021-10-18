const survey_to_delete = [];

const checkSurveyToDelete = function () {
	const btn = $(this);
	$(document).ready(function () {
		$('button').click(function () {
			const dataId = btn.attr('id');
			const dataName = btn.attr('name');
			survey_to_delete[dataId] = dataName			
		})
		// const survey_to_delete = $.map(survey_to_delete, function (dataName){
		// 	return dataName;
		// })
	})
}

$(() => {
	checkSurveyToDelete();
	$('button').on('click', () => {
		console.log(survey_to_delete)
	})
	
});
