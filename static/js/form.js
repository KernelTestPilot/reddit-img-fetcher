$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				name : $('#nameInput').val(),
			},
			type : 'POST',
			url : '/process',
			
		})
		.done(function(data) {
			
			if (data.error) {
				
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$redditnames = data.name;
				console.log($redditnames[2])
				$('.content').remove();
				$.each($redditnames, function( index, value ) {

					$('#test').append("<div class='content'> <img id='image' src="+value+"> </img> </div>");
				  });

				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});
