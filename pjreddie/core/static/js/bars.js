$(function(){

	var green = $('div.green');
	var blue = $('div.blue');
	var light = $('div.light');
	
	function transition(){
		r = Math.round(Math.random()*10);
		green.css('box-shadow', '0px 0px 100px ' + r + 'px #0f0');
		r = Math.round(Math.random()*10);
		blue.css('box-shadow', '0px 0px 100px ' + r + 'px #0ff');
		p = Math.random()*100;
	}

	var t = setInterval(transition, 1000);

});
