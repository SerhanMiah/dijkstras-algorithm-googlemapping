from flask import Flask, render_template, request
import googlemaps
from datetime import datetime

app = Flask(__name__)
gmaps = googlemaps.Client(key='YOUR_API_KEY')


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/directions', methods=['POST'])
def directions():
    origin = request.form['origin']
    destination = request.form['destination']
    now = datetime.now()

    directions_result = gmaps.directions(origin,
                                         destination,
                                         mode="driving",
                                         departure_time=now)

    return render_template('directions.html', directions=directions_result[0])



if __name__ == '__main__':
    app.run(debug=True)
