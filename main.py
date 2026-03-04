from flask import Flask, render_template, request
from database import create_database
from database_functions import *

app = Flask(__name__)
app.secret_key = 'assignment#5'

# Ensuring the database is created before handling requests
create_database()


@app.route('/', methods=['GET', 'POST'])
def index():
    '''Handle the main page and form submission'''
    errors = []
    if request.method == 'POST':
        TVOC = request.form.get('TVOC')
        eCO2 = request.form.get('eCO2')
        timestamp = request.form.get('timestamp')
    return render_template('index.html', errors=errors)


@app.route('/measurements')
def measurements_list():
    measurements = get_entries()
    return render_template('measurementsList.html', measurements=measurements)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
