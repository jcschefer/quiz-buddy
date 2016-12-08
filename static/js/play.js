// Jack Schefer, began 10/21/16 
//
// Handle the joining of rooms
//
$( document ).ready( function() {
   //
   console.log('play.js loaded')
   //
   var socket = io.connect('http://' + document.domain + ':' + location.port) ;
   socket.on('connect', function(){
      socket.emit('connection');
      socket.emit('joined_room');
   });
   //
   $( '#button' ).on('click', function(){
      socket.emit('click');
   });
   //
   socket.on('message', function(data){
      console.log(data['msg']);
   });
   //
}) ;
//
//
//
//
//
// End of file.
