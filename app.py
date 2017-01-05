# Jack Schefer
#
from flask          import Flask, render_template, request, session
from flask_socketio import SocketIO, emit
from os             import getenv, urandom
#
app = Flask( __name__ )
app.secret_key = urandom( 24 )
socketio = SocketIO( app )
#
class Player:
    #
    def __init__( name ):
        #
        self.name  = name
        self.score = 0
        #
    #
    def get_name( self ): return self.name
    def get_score( self ): return self.score
    def __lt__( self, other ): return self.score < other.score
    #
#
players = []
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
@app.route('/play.html', methods = ['POST'])
def play():
    #
    name = request.form['screen_name']
    session[ 'name' ] = name
    return render_template( 'play.html', name = name )
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
@socketio.on('joined_room')
def join():
    #
    room = session.get( 'room' )
    emit( 'message', { 'msg': session[ 'name' ] + ' has entered the room.' })
    print(session.get('name'), 'has entered the room.')
    #
#
@socketio.on('spacebar')
def pause_all_answers():
    #
    print('spacebar pressed')
    
    #
#
#
########################################################################################
# APP RUNNING
########################################################################################
if __name__ == '__main__':
    #
    #app.run( port = int(getenv( 'PORT' )) , debug = True )
    socketio.run( app, debug = True, host = '0.0.0.0', port = int( getenv('PORT', 5000)) )
    #
#
# End of file.
