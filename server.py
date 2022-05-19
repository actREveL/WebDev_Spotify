# flask nutzen (pip install flask, oder zum install auf der flask-Homepage schauen)
from datetime import date
from flask import Flask, request, jsonify, render_template
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
data = pd.read_csv('WebDev_Spotify\static\charts_only_monday_top200.csv').drop(
    ['Unnamed: 0', 'Unnamed: 0.1'], axis=1).set_index('region')

    
@app.route('/')
def index():
    return render_template('index.html')

# unsere Datenquelle / "API", liefert im Moment Daten nach Land aus (Land wird als Argument an die URL gehängt)


@app.route('/api')
def api():
    # TODO hier sollte man auch noch nach Datum die Daten filtern



    # gesuchte Region aus der URL holen
    suchregion = request.args.get('region', 'Switzerland')

    # Daten für eine Region aus der Tabelle holen (dafür ist der Index da)
    result = data.loc[suchregion]

    # Daten in json übersetzen
    track_data = []
    for index, row in result.iterrows():
        track = {"Rank": row['rank'],
                 "Title": row['title'],
                 "Artist": row['artist'],
                 "Date": row['date'],
                 "Region": index,
                 "Streams": row['streams'],
                 "URL": row['url']
                 }
        track_data.append(track)

    # region_data = track_data.index()
    # for index, row in result.iterrows():
        # country = index
        # return country
    
    # zurücksenden
    return jsonify(track_data)  # country=country

# Start von dem Flask Server
app.run(debug=True)
