# Jack Schefer
#
from flask          import Flask, render_template, session
from flask_socketio import SocketIO, join_room, emit
from os             import getenv
#
app = Flask( __name__ )
socketio = SocketIO( app )
#
########################################################################################
# APP ROUTING
########################################################################################
@app.route('/')
@app.route('/index.html')
def index():
    #
    return render_template( 'index.html' )
    #
#
@app.route('/about.html')
def about():
    #
    return render_template( 'about.html' )
    #
#
@app.route('/play.html')
def play():
    #
    return render_template( 'play.html' )
    #
#
########################################################################################
# SOCKET FUNCTIONS
########################################################################################
#
@socketio.on('click')
def handleclick():
    #
    print('it got clicked')
    #
#
@socketio.on('connection')
def connect():
    #
    print('socket connected')
    #
#
@socketio.on('joined_room')
def join():
    #
    room = session.get( 'room' )
    join_room( room )
    emit( 'message', { 'msg': session.get( 'name' ) + ' has entered the room.' } , room = room )
    print(session.get('name'), 'has entered the room.')
    #
#
########################################################################################
# APP RUNNING
########################################################################################
if __name__ == '__main__':
    #
    #app.run( port = int(getenv( 'PORT' )) , debug = True )
    socketio.run( app, debug = True )
    #
#
# End of file.
