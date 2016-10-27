// Jack Schefer, began 10/21/16 
//
// Handle the joining of rooms
//
$( document ).ready( function() {
   //
   var socket = io.connect('http://' + document.domain + ':' + location.port) ;
   socket.on('connect', function(){
      socket.emit('connection');
   });
   //
   $( '#button' ).on('click', function(){
      socket.emit('click');
   });
   //
}) ;
//
//
//
//
//
// End of file.
