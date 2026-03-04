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


if __name__ == '__main__':
    app.run(debug=True)
