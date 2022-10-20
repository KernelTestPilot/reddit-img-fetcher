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
				$reddittitles = data.title;

				const m = data.title;
				console.log(m)
				$('.content').remove();
				$.each(data.name, function( index, value ) {
					const title =m[index];
					console.log(index)
					$('#test').append("<div class='content'> <img id='image' src="+value+"> <div class='content-overlay'><h2>"+title+"</h2> </div> </img> </div>");
					
				  });

				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});
