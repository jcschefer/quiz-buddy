// Jack Schefer, began 10/21/16 
//
// Handle the joining of rooms
//
$( document ).ready( function() {
   //
   console.log('play.js loaded')
   //
   var socket = io.connect('//' + document.domain + ':' + location.port) ;
   socket.on('connect', function(){
      socket.emit('joined_room');
   });
   //
   $( '#button' ).on('click', function(){
      responsiveVoice.speak("hello and welcome to the website", "UK English Male");
      socket.emit('click');
   });
   //
   socket.on('message', function(data){
      console.log(data['msg']);
   });
   //
   socket.on( 'pause', function(){
      if( responsiveVoice.isPlaying())
      {
         responsiveVoice.pause();
      }
   });
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
