$(function(){

	var green = $('hr.green');
	var blue = $('hr.blue');
	big = 0;
	
	function transition(){
		var gw, bw, trans;
		if(big){
			gw = Math.random()*20 + 80;
			bw = Math.random()*20 + 70;
			green.removeClass("big").addClass("small");
			blue.removeClass("big").addClass("small");
		}else{
			gw = Math.random()*30;
			bw = Math.random()*30;
			green.removeClass("small").addClass("big");
			blue.removeClass("small").addClass("big");
		}
		green.css('width', gw+'%');
		blue.css('width', bw+'%');
		big = 1-big;
	}

	green.bind('transitionend', transition);
	green.bind('webkitTransitionEnd', transition);
	green.bind('otransitionend', transition);

	transition();
});
