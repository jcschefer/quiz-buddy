# Jack Schefer
#
from flask          import Flask, render_template, url_for
from flask_socketio import SocketIO
from os             import getenv
#
app = Flask( __name__ )
socketio = SocketIO( app )
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
@app.route('/play.html')
def play():
    #
    return render_template( 'play.html' )
    #
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
if __name__ == '__main__':
    #
    #app.run( port = int(getenv( 'PORT' )) , debug = True )
    socketio.run( app, debug = True )
    #
#
# End of file.
