// Jack Schefer, began 10/21/16 
//
// Handle the joining of rooms
//
var CURR_ANSWER ;
var CURR_PROMPT ;
var SCORE_INCREMENT = 15 ;
var interval    ;
var TIMER_LENGTH = 8.00 ;
//
function is_correct( answer )
{
   console.log('answer: ' + CURR_ANSWER + ' given answer: ' + answer);
   if(answer.length < 2) return false ;
   return CURR_ANSWER.toUpperCase().includes( answer.toUpperCase() ) ;
}
//
function increment_score( num )
{
   var scorebox = document.getElementById('score') ;
   scorebox.innerHTML = parseInt(scorebox.innerHTML) + num ;
}
//
function append_question() 
{
   var pr = document.createElement('p') 
   pr.appendChild( document.createTextNode( CURR_PROMPT ) ) ;
   var ans = document.createElement('div');
   ans.appendChild( document.createTextNode( CURR_ANSWER ) ) ;
   //
   var div = document.createElement('div') ;
   div.className += 'question' ;
   div.appendChild(pr);
   div.appendChild(ans);
   div.appendChild(document.createElement('br'))
   div.appendChild(document.createElement('br'))
   var board = document.getElementById('game-board') ;
   //board.insertBefore(div, board.childNodes[1]) ;
   //
   $('#game-board').prepend(div).fadeIn() ;
}
//
//
$( document ).ready( function() {
   //
   console.log('play.js loaded')
   var socket = io.connect('//' + document.domain + ':' + location.port) ;
   //
   document.getElementById('score').readonly = true ;
   //
   socket.on('connect', function(){
      socket.emit('joined_room');
   });
   //
   $( '#button' ).on('click', function(){
      responsiveVoice.speak("hello and welcome to the website", "UK English Male");
      socket.emit('click');
   });
   //
   socket.on('message', function( data ){
      console.log(data['msg']);
   });
   //
   socket.on( 'pause', function(){
      if( responsiveVoice.isPlaying())
      {
         responsiveVoice.pause();
      }
      else
      {
         console.log('** tried to pause when it\'s not playing') ;
      }
   });
   //
   socket.on( 'hearbeat', function(){
      socket.emit('heartbeat') ;
   });
   //
   socket.on( 'resume', function(){
      responsiveVoice.resume() ;
   }) ;
   //
   socket.on( 'resume', function(){
      responsiveVoice.resume() ;
   });
   //
   socket.on( 'incoming_question', function( q ){
      //responsiveVoice.cancel() ;
      var txtfield = document.getElementById("answer-box") ;
      txtfield.readonly = true ;
      txtfield.value = "" ;
      //
      console.log( 'question received' );
      console.log( q );
      //
      CURR_ANSWER = q['answer'] ;
      CURR_PROMPT = q['prompt'] ;
      //
      responsiveVoice.speak( q['prompt'], 'UK English Male', {
         'onstart': function(){ console.log('** started saying stuff');}, 
         'onend': function(){ 
            console.log('** stopped saying stuff');
            socket.emit('question_over' );},
         'onerror': function(){ console.log('** there was an error?');}
      } );
   });
      //responsiveVoice.speak( data['q'], 'UK English Male', {onend: function(){socket.emit('question_over')} } );
   //
   document.body.onkeyup = function(e){
      //
      var txtfield = document.getElementById("answer-box") ;
      //
      if( e.keyCode == 32 ) //Spacebar pressed to answer question
      {
         console.log(CURR_ANSWER);
         //socket.emit('spacebar');
         if( !responsiveVoice.isPlaying())
            return ;
         //
         responsiveVoice.pause() ;
         //
         txtfield.readOnly = false ;
         txtfield.focus() ;
         //
         var timer = TIMER_LENGTH ;
         interval = setInterval(function() {
            document.getElementById("timer").innerHTML = Number(timer).toFixed(2) ;
            timer -= 0.01 ;
            //
            if( timer <= 0 )
            {
               if( is_correct(txtfield.value))
               {
                  console.log("it's right");
                  socket.emit('get_question') ;
                  increment_score( SCORE_INCREMENT ) ;
               }
               else 
               {
                  socket.emit('get_question') ;
               }
               //
               append_question() ;
               //
               clearInterval( interval ) ;
            }
         }, 10);
         //
      }
      else if( e.keyCode == 13 ) //enter pressed to submit anser
      {
         if( txtfield.readOnly == true )
            return ;
         //
         if( is_correct( txtfield.value ) )
         {
            console.log("it's right");
            socket.emit('get_question') ;
            responsiveVoice.cancel() ;
            increment_score( SCORE_INCREMENT ) ;
         }
         // end the clock, reduce score, make text field read only, resume
         append_question() ;
         //
         clearInterval( interval ) ;
         document.getElementById("timer").innerHTML = Number(TIMER_LENGTH).toFixed(2) ;
         //
         increment_score( -5 ) ;
         //
         txtfield.readOnly = true ;
         //
         responsiveVoice.resume() ;
      }
   };
   //
}) ;
//
//
//
//
// End of file.
