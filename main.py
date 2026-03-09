# from webbrowser import get
from flask import Flask, render_template, request
import database

app = Flask(__name__)
app.secret_key = 'assignment#5'

# Ensuring the database is created before handling requests
database.create_database()


@app.route('/', methods=['GET'])
def index():
    '''Handle the main page'''
    last_measurement = database.get_last_measurement()
    highest_TVOC_measurement = database.get_highest_TVOC_measurement()
    highest_eCO2_measurement = database.get_highest_eCO2_measurement()
    lowest_TVOC_measurement = database.get_lowest_TVOC_measurement()
    lowest_eCO2_measurement = database.get_lowest_eCO2_measurement()
    return render_template('index.html', last_measurement=last_measurement, highest_TVOC_measurement=highest_TVOC_measurement,
                           highest_eCO2_measurement=highest_eCO2_measurement, lowest_TVOC_measurement=lowest_TVOC_measurement, lowest_eCO2_measurement=lowest_eCO2_measurement)


@app.route('/measurements', methods=['GET'])
def measurements_list():
    '''Display the list of measurements'''
    measurements = database.get_all_measurements()
    return render_template('measurementsList.html', measurements=measurements)


@app.route('/add_measurement', methods=['POST'])
def add_measurement():
    '''Handle the form submission for adding a new measurement'''
    TVOC = request.form.get('TVOC')
    eCO2 = request.form.get('eCO2')
    timestamp = request.form.get('timestamp')

    if not TVOC or not eCO2 or not timestamp:
        return "Missing required fields", 400

    try:
        TVOC = int(TVOC)
        eCO2 = int(eCO2)
    except ValueError:
        return "TVOC and eCO2 must be numbers", 400

    success = database.insert_measurement(TVOC, eCO2, timestamp)
    if success:
        return "Measurement added successfully", 200
    else:
        return "Failed to add measurement", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
