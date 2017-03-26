// Jack Schefer, began 10/21/16 
//
// Handle the joining of rooms
//
var CURR_ANSWER ;
var interval    ;
//
function is_correct( answer )
{
   return CURR_ANSWER.includes( answer ) ;
}
//
//
$( document ).ready( function() {
   //
   console.log('play.js loaded')
   var socket = io.connect('//' + document.domain + ':' + location.port) ;
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
   });
   socket.on( 'resume', function(){
      responsiveVoice.resume() ;
   });
   //
   socket.on( 'incoming_question', function( q ){
      //responsiveVoice.cancel() ;
      console.log( 'question received' );
      console.log( q );
      //
      CURR_ANSWER = q['answer'] ;
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
         var timer = 5.0 ;
         interval = setInterval(function() {
            document.getElementById("timer").innerHTML = Number(timer).toFixed(3) ;
            timer -= 0.01 ;
            //
            if( timer <= 0 )
            {
               if( is_correct(txtfield.value))
                  console.log("it's right");
               clearInterval( interval ) ;
            }
         }, 1);
         //
      }
      else if( e.keyCode == 13 ) //enter pressed to submit anser
      {
         if( txtfield.readOnly == true )
            return ;
         //
         if( is_correct( txtfield.value ) )
         {
            //stop the clock, add to score, new question
            socket.emit('answered_correct') ;
         }
         else
         {
            // end the clock, reduce score, resume
            socket.emit('answered_wrong')
         }
      }
   };
   //
}) ;
//
//
//
//
// End of file.
