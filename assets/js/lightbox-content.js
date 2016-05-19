(function(){

	var lastVisitedLink;

	$('.page-content ul a').featherlight({
		type: 'iframe', 
		iframeWidth: '100%',
	    iframeHeight: '100%'
	}).click( function(){
		
		if( lastVisitedLink ){
			$(lastVisitedLink).css('background', 'transparent');
		}

		$(this).css('background', 'rgba(0,0,0,0.1)');
		lastVisitedLink = $(this);
	});

})();

