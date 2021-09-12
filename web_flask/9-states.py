#!/usr/bin/python3
''' starts a Flask web app '''


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    ''' displays HTML page of state objects sorted by name '''
    states = storage.all('State')
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    ''' displays HTML page of state objects sorted by name '''
    for state in storage.all('State').values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def close_connection():
    ''' closes the session '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
