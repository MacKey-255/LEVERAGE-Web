function countdown(secondsRemaining) {

	var days = Math.floor(secondsRemaining / 86400),
	    hours = Math.floor((secondsRemaining - (days * 86400)) / 3600),
	    minutes = Math.floor((secondsRemaining - (days * 86400) - (hours * 3600)) / 60),
	    seconds = secondsRemaining - (days * 86400) - (hours * 3600) - (minutes * 60);
	    
	if(secondsRemaining > 0) {
	
		if(days < 10) { days = '0' + days; }
		if(hours < 10) { hours = '0' + hours; }
		if(minutes < 10) { minutes = '0' + minutes; }
		if(seconds < 10) { seconds = '0' + seconds; }
		
		$('.days > .number').html(days);
		$('.hours > .number').html(hours);
		$('.minutes > .number').html(minutes);
		$('.seconds > .number').html(seconds);
		
		secondsRemaining--;
		
	} else {
	
		if(secondsRemaining == 0) {
	
			window.location.reload();
		
		}
		
	}
	window.setTimeout(function() {
	
   		countdown(secondsRemaining);
   		
	}, 1000);
	
}
function updateProgress(procent) {

	if(typeof procent !== "number") {
		procent = 0;
	}

	if(procent <= 7) {
		
		$('.progressBarFill').css({ width: '7%' }).find('.progressBarFillMiddle').html(procent + '%');
		
	} else if(procent >= 100) {
	
		$('.progressBarFill').css({ width: '100%' }).find('.progressBarFillMiddle').html('100%');
	
	} else {
	
		$('.progressBarFill').css({ width: procent + '%' }).find('.progressBarFillMiddle').html(procent + '%');
		
	}

}
function objectConverter(array) {

	var object = {};
	for(var i=0; i<array.length; i++) {
		object[array[i]] = '';
	}
	return object;
	
}
function setHeaderColor(color) {

	color = color.toLowerCase();

	if(typeof color === "undefined") {
		color = 'yellow';
	}
	
	if(color in objectConverter(['green', 'blue', 'yellow', 'purple', 'red', 'gray'])) {
	
		$('.header').attr('class', 'header').addClass(color);
	
	}

}
function setProgressFillColor(color) {

	color = color.toLowerCase();

	if(typeof color === "undefined") {
		color = 'green';
	}
	
	if(color in objectConverter(['green', 'blue', 'yellow', 'purple', 'red', 'gray'])) {
	
		$('.progressBarFill').attr('class', 'progressBarFill clear').addClass(color);
	
	}

}