#!/usr/bin/python3
''' starts a Flask web app '''


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    ''' displays HTML page of state objects sorted by name '''
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close_connection():
    ''' closes the session '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
