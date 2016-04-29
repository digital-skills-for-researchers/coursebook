$(document).ready(function() {


	// get all children of the module element
	var moduleInfoContainer = $('.page-content');
	var moduleChildElements = moduleInfoContainer.children();
	var sectionChildren = [];

	moduleChildElements.each( function(index, element) {

		element = $(element);

		// every time we reach an h1 or h2,
		// or reach the end of the list,
		// create a new section and dump all
		// collected elements into it
		if( element.is("h1, h2") ){

			// if there are children collected
			if( sectionChildren.length > 0 ){

				// publish the last group
				var newSection = $("<section></section>");
				newSection.addClass("container")
				newSection.append(sectionChildren);
				moduleInfoContainer.append(newSection);

				// start a new group
				sectionChildren = [];
			}
			

		}

		sectionChildren.push(element);

		// if that was the last item, publish anyway
		if( index == moduleChildElements.length-1) {
			// publish the last group
			var newSection = $("<section></section>");
			newSection.addClass("container")
			newSection.append(sectionChildren);
			moduleInfoContainer.append(newSection);
		}

	});

});