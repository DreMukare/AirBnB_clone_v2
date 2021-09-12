#!/usr/bin/python3
''' starts a Flask web app '''


from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    ''' displays HTML page '''
    data = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('7-states_list.html', data=data)


@app.teardown_appcontext
def close_connection():
    ''' closes the session '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
