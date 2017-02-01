# Jack Schefer
#
from flask          import Flask, render_template, send_from_directory, request, session
from flask_socketio import SocketIO, emit
from os             import getenv, path, urandom
from sys            import argv
#
app = Flask( __name__ )
#app.config['SECRET_KEY'] = b'\x01t;2\xb1\xb4\xd9w\xaf\xf1\x12\xbd\xe3D\xff\xb2\xc8\xbc\xdc\xe6\xd3\x93\x85'
socketio = SocketIO( app )
#
fname = path.join( path.dirname( path.abspath( argv[ 0 ] ) ), 'secret_key' )
if not path.isfile( fname ):
    #
    print('Error: no secret key, making new one')
    with open( fname, 'wb' ) as newf: newf.write( urandom( 24 ) )
    #
with open( fname, 'rb' ) as f: app.config[ 'SECRET_KEY' ] = f.read()
#
class Player:
    #
    def __init__( self, n ):
        #
        self.name  = n
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
@app.route('/storm/map/')
def serve_map():
    #
    #return app.send_from_directory('static/storm-tracker', filename)
    return app.send_static_file('storm-tracker/map.html')
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
    emit( 'message', { 'msg': session[ 'name' ] + ' has entered the room.' }, broadcast = True )
    #
    p = Player( session['name'] )
    players.append( p )
    #
    print(session.get('name'), 'has entered the room.')
    #
#
@socketio.on('spacebar')
def pause_all_answers():
    #
    print('spacebar pressed')
    emit( 'message', {'msg': session[ 'name' ] + 'has buzzed in.'}, broadcast = True )
    emit( 'pause', broadcast = True )
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
