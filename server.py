# flask nutzen (pip install flask, oder zum install auf der flask-Homepage schauen)
import datetime
from datetime import date
# from aiohttp import TraceDnsCacheHitParams
from flask import Flask, request, jsonify, render_template, make_response
import csv
import pandas as pd
import json
# from IPython.display import display, HTML

# from flask_wtf import Form
# from wtforms import DateField

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

# unsere Datenquelle / "API", liefert im Moment Daten nach Land aus (Land wird als Argument an die URL gehängt)


@app.route('/api')
def api():
    # TODO hier sollte man auch noch nach Datum die Daten filtern
    # dates = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in data['date']]
    # dates.sort()
    # sorteddates = [datetime.datetime.strftime(ts, "%Y-%m-%d") for ts in dates]


    # gesuchte Region aus der URL holen / http://127.0.0.1:5000/api?region=Argentina&date=2017-01-02
    suchregion = request.args.get('region', 'Switzerland')
    suchdate = request.args.get('date', '2017-01-02')

    # Daten für eine Region aus der Tabelle holen (dafür ist der Index da)
    result = data[(data.region == suchregion) & (data.date == suchdate)]  #sorteddates

    # Daten in json übersetzen
    #track_data = []
    #for index, row in result.iterrows():
    #    track = {"Rank": row['rank'],
    #             "Title": row['title'],
    #             "Artist": row['artist'],
    #             "Date": row['date'],
    #             "Region": index,
    #             "Streams": row['streams'],
    #             "URL": row['url']
#                 }
    #    track_data.append(track)
    track_data = result.to_json(orient="records")

    # region_data = track_data.index()
    # for index, row in result.iterrows():
        # country = index
        # return country
    
    # zurücksenden

    response = make_response(track_data)
    response.mimetype = "application/json"
    return response
    #return jsonify(track_data)  # country=country

@app.route('/apicountry')
def apicountry():
    countries=data.region.unique().tolist()
    return jsonify(countries)

# Start von dem Flask Server
app.run(debug=True)
