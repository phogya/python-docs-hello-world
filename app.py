from flask import Flask
from flask import render_template
import json
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    response = requests.get("https://waterservices.usgs.gov/nwis/dv/?format=json&sites=04213500&period=P1D&siteStatus=all")
    jsponse = response.json()

    data = []

    for datapoint in jsponse["value"]['timeSeries']:
        
        var_unit = datapoint['variable']["unit"]["unitCode"]
        var_desc = datapoint['variable']["variableDescription"]
        var_option = datapoint['variable']["options"]["option"][0]['value']
        
        var_value = datapoint['values'][0]['value'][0]['value']
        
        data.append([var_value, var_unit, var_desc, var_option])

    return render_template("index.html", data=data)
    #return str(response.json())
