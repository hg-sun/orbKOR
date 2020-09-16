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
app.config['JSON_AS_ASCII'] = False
api = Api(app)

current_path = os.path.dirname(os.path.abspath(__file__))
global_config = ConfigMgr(os.path.join(current_path, 'orbKOR'))
ok = OrbKOR()

#Append Mode
@app.route('/extract-clade', methods=['POST'])
def extractClade():
    input_data = request.get_json(force=True)
    data = input_data['data']
    if ok.parse(data):
        clades = ok.getClade()
        if len(clades) != 0:
            ret = "|".join(clades)
        else:
            ret = 'No Clade Matched'
    else:
        ret = 'No Matched Sentence'
    return jsonify(ret)

@app.route('/')
def index():
    return 'Connection Succeeded'

if __name__ == "__main__":
    host = global_config.getValue('COMMON', 'common.host')
    port = global_config.getValue('COMMON', 'common.port')
    app.run(host=host, port=port, debug=False)

