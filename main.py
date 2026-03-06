from flask import Flask, render_template, request
from database import create_database
from database_functions import *

app = Flask(__name__)
app.secret_key = 'assignment#5'

# Ensuring the database is created before handling requests
create_database()


@app.route('/', methods=['GET'])
def index():
    '''Handle the main page'''
    last_measurement = {
        'TVOC': 300, 'eCO2': 400, 'timestamp': '06.03.2026 12.23'}
    highest_measurement = {
        'TVOC': 500, 'eCO2': 600, 'timestamp': '05.03.2026 11.00'}
    lowest_measurement = {
        'TVOC': 100, 'eCO2': 200, 'timestamp': '04.03.2026 10.00'
    }
    return render_template('index.html', last_measurement=last_measurement, highest_measurement=highest_measurement, lowest_measurement=lowest_measurement)


@app.route('/measurements', methods=['GET'])
def measurements_list():
    '''Display the list of measurements'''
    measurements = [
        {'TVOC': 300, 'eCO2': 400, 'timestamp': '06.03.2026 12.23'},
        {'TVOC': 500, 'eCO2': 600, 'timestamp': '05.03.2026 11.00'},
        {'TVOC': 100, 'eCO2': 200, 'timestamp': '04.03.2026 10.00'}
    ]
    return render_template('measurementsList.html', measurements=measurements)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
