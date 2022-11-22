$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				name : $('#nameInput').val(),
				type : $('#type').val(),
			},
			type : 'POST',
			url : '/process',
			
		})
		.done(function(data) {
			
			if (data.error) {
				
				$('#errorAlert').text(data.error).show();
				console.log("rate limit")
			}
			else {
				const m = data.title;
			
				$('.swiper-slide').remove();
				$.each(data.name, function( index, value ) {
					const title =m[index];
					
					$('#test').append("<div class='swiper-slide slide'><div class='content'> <img id='image' src="+value+"> <div class='content-overlay'><h2>"+title+"</h2> </div> </img> </div></div>");
					
				  });

				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});
