/*
*
Author: Tanya Gray

Sidenotes is a plugin for reveal.js which displays
speaker notes in a docked sidebar, visible to the
viewer.

Version: 0.1
 
License: MIT license (see LICENSE.md)
*
*/
window.Sidenotes || (window.Sidenotes = function (Reveal) {

	var noNotesMessage = "<p><i>Sorry, no notes for this slide!</i></p>";

	var sidenotesOpen,
		slideshow,
		notesPanel;


	// Reveal event bindings
	Reveal.addEventListener('ready', init);
	Reveal.addEventListener('slidechanged', updateNotes);



	/*
	Only set up Sidenotes once Reveal is ready
	*/
	function init(event) {
		getSlideshow();
		createNotesPanel();
		updateNotes();
		loadCookies();
		layout();
		bindKeys();
	}


	/*
	Get a reference to the slideshow's parent container, 
	which is where we will add the sidenotes.
	*/
	function getSlideshow() {
		slideshow = $('.sidenotes').parent();
	}


	/*
	Adds a div inside the slideshow which will contain
	the speaker notes.
	*/
	function createNotesPanel() {

		notesPanel = $('.sidenotes');

		if(!notesPanel) {
			notesPanel = $('<div></div>');
			notesPanel.addClass('sidenotes');
			slideshow.append(notesPanel);
		}
	}


	/*
	Copy notes to visible notes section
	*/
	function updateNotes() {
		slide = Reveal.getCurrentSlide();
		notes = $(slide).find('aside.notes').html();

		if(notes.trim().length == 0){
			notes = noNotesMessage;
		}

	    $('.sidenotes .content').html(notes);
	}


	/*
	Check cookies for whether the sidenotes were previously open
	*/
	function loadCookies() {
		sidenotesOpen = Cookies.get('sidenotes') == 'true';
	}


	/*
	Save sidenotes state in cookies to allow persistence
	on other pages.
	*/
	function setCookies() {
		Cookies.set('sidenotes', sidenotesOpen);
	}


	/*
	Fairly self-explanatory...
	*/
	function toggleSidenotes() {
		
		sidenotesOpen = !sidenotesOpen;
		layout();

		return sidenotesOpen;
	}


	/*
	Use the stored state to show or hide the sidenotes as needed
	*/
	function layout() {

		if(sidenotesOpen) {
			slideshow.addClass("with-notes");
		} else {
			slideshow.removeClass("with-notes");
		}

		// layout reveal once the transition is complete
		// TODO: make this resizing smooth
		slideshow.one(
			'webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend',   
    		Reveal.layout
    	);

		setCookies();
	}


	/*
	Watch for key presses in the window
	*/
	function bindKeys() {
		// document event bindings
		$(document).keypress( onKeypress );
	}


	/*
	Allow the user to toggle sidenotes using the enter key
	*/
	function onKeypress(event) {
		if(event.which == 13) 
			toggleSidenotes();
	}

	
	toggle = toggleSidenotes;

	return this;
	

}(Reveal));
