# Jack Schefer
#
from flask          import Flask, render_template, send_from_directory, request, session
from flask_socketio import SocketIO, emit
from json           import load
from os             import getenv, path, urandom
from random         import choice
from sys            import argv
from time           import time
#
QUESTION_FILENAME = 'parser/formatted_small_tournaments.json'
#
app = Flask( __name__ )
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
    def __str__( self ): return self.name
    #
#
last_buzz = time() 
playing = False
players = []
try: 
    with open( QUESTION_FILENAME ) as f: questions = load( f )
except: print('cannot find json file of questions')
#
########################################################################################
# APP ROUTING
########################################################################################
#
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
@app.route('/onefile')
def serve_map():
    #
    return render_template('onefile.html')
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
@socketio.on('answered_correct')
def handle_correct():
    #
    #sm about points and such
    
    on_question_over()
    #
#
@socketio.on('answered_wrong')
def handle_wrong():
    #
    emit( 'resume' )
    #
#
@socketio.on('question_over')
def on_question_over():
    #
    emit( 'incoming_question', get_random_question(), broadcast=True )
    #emit( 'incoming_question', { 'q': choice(['hey', 'what is up', 'hello', 'my name is jeff']) }, broadcast=True )
    #emit( 'incoming_question', { 'q': questions[7][1][0][1][0][0] }, broadcast = True)
    #
#
@socketio.on('joined_room')
def join():
    #
    emit( 'message', { 'msg': session[ 'name' ] + ' has entered the room.' } )
    #
    p = Player( session['name'] )
    players.append( p )
    #
    #emit( 'message', { 'msg': '***players: ' + ', '.join(pl.get_name() for pl in players) }, broadcast = True )
    #
    #emit( 'incoming_question', { 'q': 'first thing\'s first' } )
    emit( 'heartbeat' )
    emit( 'incoming_question', questions[2]['questions'][1] )
    #
    #global playing
    #playing = True
    #
    print( session.get('name'), 'has entered the room.' )
    #
#
@socketio.on('spacebar')
def pause_all_answers():
    #
    print('spacebar pressed')
    last_buzz = time()
    emit( 'message', {'msg': session[ 'name' ] + 'has buzzed in.'} )
    emit( 'pause' )
    #
#
@socketio.on( 'heartbeat' )
def stay_alive():
    #
    emit('message', {'msg': 'heartbeat'} )
    emit( 'heartbeat' )
    #
#
########################################################################################
# OTHER HELPER FUNCTIONS
########################################################################################
#
def get_random_question():
    #
    while True:
        try: 
            r = choice(questions)
            q = choice(r['questions'])
            return q
        except: pass
    #
#
########################################################################################
# APP RUNNING
########################################################################################
#
if __name__ == '__main__':
    #
    #app.run( port = int(getenv( 'PORT' )) , debug = True )
    socketio.run( app, debug = True, host = '0.0.0.0', port = int( getenv('PORT', 5000)) )
    #
#
# End of file.
