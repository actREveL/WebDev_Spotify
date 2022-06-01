from datetime import date
from flask import Flask, request, jsonify, render_template, make_response
import pandas as pd

# Flask-App erzeugen
app = Flask(__name__)


# im Server laden wir alle Daten, pandas wird genutzt
# unnütze Spalten werden gelöscht
# index auf Region zum schnellen Nachschlagen
data = pd.read_csv('static/charts_only_monday_top200.csv', parse_dates=[4]).drop(
    ['Unnamed: 0', 'Unnamed: 0.1'], axis=1)

    
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api')
def api():
    # gesuchte Region aus der URL holen / http://127.0.0.1:5000/api?region=Argentina&date=2017-01-02
    suchregion = request.args.get('region', 'Switzerland')
    suchdate = request.args.get('date', '2017-01-02')

    # Daten für eine Region aus der Tabelle holen (dafür ist der Index da)
    result = data[(data.region == suchregion) & (data.date == suchdate)]

    track_data = result.to_json(orient="records")
    
    # zurücksenden
    response = make_response(track_data)
    response.mimetype = "application/json"
    return response


@app.route('/apicountry')
def apicountry():
    countries=data.region.unique().tolist()
    return jsonify(countries)

# Start Flask Server
app.run(debug=True)
