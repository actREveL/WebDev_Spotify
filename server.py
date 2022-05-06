# flask nutzen (pip install flask, oder zum install auf der flask-Homepage schauen)
from flask import Flask, request, jsonify, render_template

# Flask-App erzeugen
app = Flask(__name__)

# unsere Hauptseite, liegt jetzt im Ordner templates
@app.route('/')
def index():
    return render_template('index.html')

# unsere Datenquelle / "API", liefert im Moment Daten nach Land aus (Land wird als Argument an die URL gehängt)
@app.route('/api')
def api():

    # Rohdaten, die müsst Ihr aus Euerer Datenquelle lesen (TODO)
    data = []
    with open("static\charts_final.csv", "r") as file:
        for row in data:
            Rank, Title, Artist, Date, Region, Streams, URL = row.split(",")
            track = {"Rank": Rank,
            "Title": Title,
            "Artist": Artist,
            "Date": Date,
            "Region": Region,
            "Streams": Streams,
            "URL": URL
            }
            data.append(track)

    return jsonify(data)


    # nur die Zeilen auswählen, die dem gesuchten Land entsprechen
    #result = []
    #for row in data:
       #if row[4] == land:
           #result.append(row)

    # Daten als JSON-Text ausliefern (kann man im Browser gut anschauen)
    #return jsonify(data)

# Start von dem Flask Server
app.run(debug=True)