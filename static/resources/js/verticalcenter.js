$(document).ready(function() {

	changeContainerPosition();
	
	$(window).bind("resize", function(){
	    changeContainerPosition();
	});
	
	function changeContainerPosition() {
	
		var windowHeight = $(window).height();
		var containerHeight = $('.container').height() - $('.container > .logo').height() + $('.container > .bottomBar').height();
		var calculate = (windowHeight - containerHeight) / 2;
		calculate -= $('.container > .logo').height();
		calculate += $('.container > .bottomBar').height();
		
		if(calculate >= 0) {
			$('.container').css({ margin: calculate + 'px auto 0 auto' });
		}
	
	}

});