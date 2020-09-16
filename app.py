#Python Library
import os, sys
import json
import csv
import requests

#Flask Library
from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api

from orbKOR.OrbKOR import OrbKOR
from orbKOR.ConfigMgr import ConfigMgr

app = Flask(__name__, static_url_path='/static')
api = Api(app)

current_path = os.path.dirname(os.path.abspath(__file__))
ok = OrbKOR()

#Append Mode
@app.route('/extract-clade', methods=['POST'])
def extractClade():
    input_data = request.get_json(force=True)
    data = input_data['data']
    ok.parse(data)
    clades = ok.getClade()
    ret = "|".join(clades)
    return jsonify(ret)

@app.route('/')
def index():
    return 'Connection Succeeded'

if __name__ == "__main__":
    host = global_config.getValue('COMMON', 'common.host')
    port = global_config.getValue('COMMON', 'common.port')
    app.run(host=host, port=port, debug=False)

