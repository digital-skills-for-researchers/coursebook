$(document).ready(function() {

	var calendar = $('.calendar');

	if( calendar ){
		convertCalendarToList();
	}


	function convertCalendarToList() {

		// create a collapsible list
		var collapsibleList = createCollapsibleList();

		// get all children of the module element
		var calendarChildElements = calendar.children();

		var startIndex;
		var endIndex;

		calendarChildElements.each( function(index, element) {

			element = $(element);

			// scan for index of h3
			if(element.is("h3")) startIndex = index;

			// scan for index of table
			if(element.is("table")) endIndex = index;

			// when we've found the start and end indices
			// of the elements which should be in the row
			if( startIndex && endIndex) {

				// collect elements by index
				elements = calendarChildElements.slice(startIndex, endIndex+1);

				// create a list item
				listItem = $('<li></li>');

				// create a header and add the h3
				h3 = elements.slice(0,1);
				header = createListItemHeaderWithContent(h3);
				listItem.append(header);

				// create a body and add the other stuff
				bodyChildren = elements.slice(1);
				body = createListItemBodyWithContent(bodyChildren);
				listItem.append(body);

				// append to the list
				collapsibleList.append(listItem);
				
				// reset the indices
				startIndex = undefined;
				endIndex = undefined;
			}

		});

		// append the list to the calendar container
		calendar.append(collapsibleList);

		// initialise the collapsible list with materialize
		$('.collapsible').collapsible();
	}
	


	function createCollapsibleList(){

		list = $('<ul></ul>');

		list.addClass('collapsible popout');
		list.attr('data-collapsible', 'accordion');

		return list;
	}


	function createListItemHeaderWithContent(content){

		header = $('<div></div>');

		header.addClass('collapsible-header');
		header.append(content);

		return header;

	}


	function createListItemBodyWithContent(content){

		body = $('<div></div>');

		body.addClass('collapsible-body');
		body.append(content);

		return body;
	}



});