$(document).ready( function(){

	var deepLink = window.location.hash;
	var element = $(deepLink);

	if( element.length !== 0 ){

		// highlight the element's section
		element.parent().css('background', 'lavender');

		// scroll to the element
		$('html, body').animate({
		    scrollTop: (element.offset().top - 100) // leave 100px gap from top
		},500);
	}

});
