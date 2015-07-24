$(document).ready(function() {
	// Setup - add a text input to each footer cell
	$('#projects-table tfoot th').each( function () {
		var title = $('#projects-table thead th').eq( $(this).index() ).text();
		$(this).html( '<input type="text" placeholder="Search '+title+'" />' );
	} );
 
	// DataTable
	var table = $('#projects-table').DataTable();
 
	// Apply the search
	table.columns().every( function () {
		var that = this;
 
		$( 'input', this.footer() ).on( 'keyup change', function () {
			that
				.search( this.value )
				.draw();
		} );
	} );

	$.fn.editable.defaults.mode = 'inline';

	$('#firstname-change').editable();
	$('#lastname-change').editable();
	$('#email-change').editable();
	
	// $('.selectpicker').selectpicker();

	$('#newProjectModal').on('shown.bs.modal', function(e) {
		$("#createProjectForm").one('submit', function(e) {
			e.preventDefault();
			$.ajax({
				type : "POST",
				url: "/profile",
				data: {form_name: 'create-project', name: $('#name_proj').val(), description: $('#description_proj').val()},
			}).always(function(data) {
				alert(data.statusCode);
				alert(data.responseText);
			});
		})
	});
} );

function showModal() {
    $("#change-password-modal").modal('show');
}