from flask import Flask, render_template, request, jsonify
import database
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'assignment#5'

# Ensuring the database is created before handling requests
database.create_database()


@app.route('/', methods=['GET'])
def index():
    '''Handle the main page'''

    stats = database.get_statistics()

    return render_template(
        "index.html",
        last_measurement=stats["last"],
        highest_TVOC_measurement=stats["max_TVOC"],
        lowest_TVOC_measurement=stats["min_TVOC"],
        highest_eCO2_measurement=stats["max_eCO2"],
        lowest_eCO2_measurement=stats["min_eCO2"]
    )


@app.route('/measurements', methods=['GET'])
def measurements_list():
    '''Display paginated measurements'''
    page = int(request.args.get('page', 1))
    limit = 20
    offset = (page - 1) * limit

    measurements = database.get_measurements_paginated(
        limit=limit, offset=offset)
    total_count = database.get_measurements_count()

    total_pages = (total_count + limit - 1) // limit
    return render_template('measurementsList.html', measurements=measurements, current_page=page, total_pages=total_pages)


@app.route('/add_measurement', methods=['POST'])
def add_measurement():
    '''Handle the form submission for adding a new measurement'''
    data = request.get_json()
    if not data:
        return "Invalid JSON data", 400

    TVOC = data.get('TVOC')
    eCO2 = data.get('eCO2')

    if TVOC is None or eCO2 is None:
        return "Missing required fields", 400

    try:
        TVOC = int(TVOC)
        eCO2 = int(eCO2)
    except ValueError:
        return "TVOC and eCO2 must be numbers", 400

# using strftime to format the timestamp in a way that is compatible with SQLite
    # timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    timestamp = datetime.utcnow().isoformat()

    success = database.insert_measurement(TVOC, eCO2, timestamp)
    if success:
        return "Measurement added successfully", 200
    else:
        return "Failed to add measurement", 500


@app.route("/api/statistics")
def api_statistics():
    stats = database.get_statistics()

    def row_to_dict(row):
        return dict(row) if row else None

    return jsonify({
        "latest": row_to_dict(stats["last"]),
        "min_tvoc": row_to_dict(stats["min_TVOC"]),
        "max_tvoc": row_to_dict(stats["max_TVOC"]),
        "min_eco2": row_to_dict(stats["min_eCO2"]),
        "max_eco2": row_to_dict(stats["max_eCO2"])
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
