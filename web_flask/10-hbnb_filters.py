#!/usr/bin/python3
''' starts a Flask web app '''


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    ''' displays HTML page of state objects sorted by name '''
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('9-states.html', states=states, amenities=amenities)


@app.teardown_appcontext
def close_connection():
    ''' closes the session '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
