var CURR_ANSWER ;
var CURR_TEXT ;
var SCORE_INCREMENT = 15 ;
var interval    ;
var TIMER_LENGTH = 8.00 ;
var VALID_ANSWER_TIME = false;
var QUESTION_URL = "/data/random_question";

function is_correct(answer) {
	//console.log('answer: ' + CURR_ANSWER + ' given answer: ' + answer);
	if(answer.length < 2) return false ;
	return CURR_ANSWER.toUpperCase().includes( answer.toUpperCase() ) ;
}

function increment_score(num) {
	var scorebox = document.getElementById('score') ;
	scorebox.innerHTML = parseInt(scorebox.innerHTML) + num ;
}

function append_question() {
	var pr = document.createElement('p') 
	pr.appendChild( document.createTextNode( CURR_TEXT ) ) ;
	var ans = document.createElement('div');
	ans.appendChild( document.createTextNode( CURR_ANSWER ) ) ;

	var div = document.createElement('div') ;
	div.className += 'question' ;
	div.appendChild(pr);
	div.appendChild(ans);
	div.appendChild(document.createElement('br'))
	div.appendChild(document.createElement('br'))
	div.className += ' question' ;
	var board = document.getElementById('game-board') ;

	$('#game-board').prepend(div).fadeIn() ;
	$(document).scrollTop() ;
}

function playGame() {
	var xhttp;
	try {
		xhttp = new XMLHttpRequest();
	} catch (e) {
		try {
			xhttp = new ActiveXObject("Msxml2.XMLHTTP");
		} catch(e) {
			try {
				xhttp = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (e) {
				alert("Cannot create AJAX request... :(");
			}
		}
	}

	xhttp.onreadystatechange = function() {
		if (xhttp.readyState == 4) {
			console.log(xhttp.responseText);
			var q = JSON.parse(xhttp.responseText);

			VALID_ANSWER_TIME = true;
			CURR_TEXT = q.text;
			CURR_ANSWER = q.answer;

			responsiveVoice.speak( q['text'], 'UK English Male', {
					'onend': function(){ 
					VALID_ANSWER_TIME = false;
					console.log('** stopped saying stuff');
					playGame();
					},
					'onerror': function(){ console.log('** there was an error?');}
					});
		}
	}

	xhttp.open("GET", QUESTION_URL, true);
	xhttp.send();
}

$( document ).ready( function() {

	console.log('play.js loaded')

	document.getElementById('score').readonly = true ;

	$( '#button' ).on('click', function(){
		responsiveVoice.speak("hello and welcome to the website", "UK English Male");
		socket.emit('click');
	});

	$( '#play-pause' ).on('click', function(){
		if(responsiveVoice.isPlaying())	{
			responsiveVoice.pause() ;
		} else {
			responsiveVoice.resume() ;
		}
	});

	playGame();

	document.body.onkeyup = function(e) {
		var txtfield = document.getElementById("answer-box") ;

		if( e.keyCode == 32 && VALID_ANSWER_TIME) { //Spacebar pressed to answer question 
			console.log(CURR_ANSWER);
			if( !responsiveVoice.isPlaying())
				return ;

			responsiveVoice.pause() ;

			txtfield.readOnly = false ;
			txtfield.focus() ;

			var timer = TIMER_LENGTH ;
			interval = setInterval(function() {
				document.getElementById("timer").innerHTML = Number(timer).toFixed(2) ;
				timer -= 0.01 ;

				if( timer <= 0 ) {
					if( is_correct(txtfield.value)) {
						console.log("it's right");
						increment_score( SCORE_INCREMENT ) ;
						VALID_ANSWER_TIME = false;
					}

					clearInterval( interval ) ;
				}
			}, 10);
		}

		else if( e.keyCode == 13 ) //enter pressed to submit anser
		{
			if( txtfield.readOnly == true )
				return ;

			VALID_ANSWER_TIME = false;

			if( is_correct( txtfield.value ) ) {
				console.log("it's right");
				increment_score( SCORE_INCREMENT ) ;
			} else {
				increment_score( -5 ) ;
			}

			try {
				clearInterval( interval ) ;
			} catch(err) { 
				console.log(err) ;
			}

			document.getElementById("timer").innerHTML = Number(TIMER_LENGTH).toFixed(2) ;

			txtfield.readOnly = true ;
			txtfield.value = "";
			append_question();

			playGame();
		}
	};
}) ;

// End of file.
