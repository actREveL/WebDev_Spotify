# flask nutzen (pip install flask, oder zum install auf der flask-Homepage schauen)
from flask import Flask, request, jsonify, render_template
import csv

# Flask-App erzeugen
app = Flask(__name__)

def daten():
    data = []
    with open('static/charts_only_monday_top200.csv', "r") as file:
        my_reader = csv.reader(file, delimiter=',')
        for row in my_reader:
            # title,rank,date,artist,url,region,streams
            a, b, Title, Rank, Date, Artist, URL, Region, Streams = row
            track = {"Rank": Rank,
            "Title": Title,
            "Artist": Artist,
            "Date": Date,
            "Region": Region,
            "Streams": Streams,
            "URL": URL
            }
            data.append(track)

    return jsonify(data[1:])

# unsere Hauptseite, liegt jetzt im Ordner templates
@app.route('/')
def index():
    return render_template('index.html')

# unsere Datenquelle / "API", liefert im Moment Daten nach Land aus (Land wird als Argument an die URL gehängt)
@app.route('/api')
def api():
    return daten()

    # Rohdaten, die müsst Ihr aus Euerer Datenquelle lesen (TODO)
    


    # nur die Zeilen auswählen, die dem gesuchten Land entsprechen
    #result = []
    #for row in data:
       #if row[4] == land:
           #result.append(row)

    # Daten als JSON-Text ausliefern (kann man im Browser gut anschauen)
    #return jsonify(data)

# Start von dem Flask Server
app.run(debug=True)