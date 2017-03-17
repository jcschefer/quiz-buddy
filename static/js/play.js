// Jack Schefer, began 10/21/16 
//
// Handle the joining of rooms
//
//
function question_end(){
   console.log('** stopped saying stuff');
   socket.emit(' question_over' ) ;
}
function question_start(){
   console.log('started saying stuff');
}
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
   socket.on( 'incoming_question', function( data ){
      responsiveVoice.cancel() ;
      console.log('question received');
      //
      responsiveVoice.speak( data['q'], 'UK English Male', {
         'onstart': function(){ console.log('** started saying stuff');}, 
         'onend': function(){ 
            console.log('** stopped saying stuff');
            socket.emit('question_over');
         },
         'onerror': function(){ console.log('** there was an error?');}
      } );
   });
      //responsiveVoice.speak( data['q'], 'UK English Male', {onend: function(){socket.emit('question_over')} } );
   //
   document.body.onkeyup = function(e){
      if( e.keyCode == 32 ) //Spacebar pressed to answer question
      {
         socket.emit('spacebar');
      }
   };
   //
}) ;
//
//
//
//
//
// End of file.
