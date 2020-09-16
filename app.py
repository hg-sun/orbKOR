#Python Library
import os, sys
import json
import csv
import requests
import subprocess
import time
import datetime
import pickle
from cachetools import LRUCache
from collections import OrderedDict, defaultdict

#Flask Library
from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api

#Orb Library
from orb.Orb import Orb
from orb.Logger import global_logger
from orb.ConfigMgr import ConfigMgr
from orb.OrbUtil.SpacyWrapper import SpacyWrapper
from orb.Cache import Cache
from Loader import Loader

app = Flask(__name__, static_url_path="/static")
api = Api(app)

current_path = os.path.dirname(os.path.abspath(__file__))
global_config = ConfigMgr(os.path.join(current_path, 'orb'))
#cache_dict = {}
loader = Loader(option='file_system')

# Append Mode
@app.route('/extract-sentence', methods=['POST'])
def extractSentence():
    input_data = request.get_json(force=True)
    cmd = str(request.url_rule).replace("/","")
    ret = execute(cmd=cmd, input_data=input_data)
    return jsonify(ret)

# Append Mode
@app.route('/extract-simple-sentence', methods=['POST'])
def extractSimpleSentence():
    input_data = request.get_json(force=True)
    cmd = str(request.url_rule).replace("/","")
    ret = execute(cmd=cmd, input_data=input_data)
    return jsonify(ret)

# Append Mode
@app.route('/extract-clade', methods=['POST'])
def extractClade():
    input_data = request.get_json(force=True)
    cmd = str(request.url_rule).replace("/","")
    ret = execute(cmd=cmd, input_data=input_data)
    return jsonify(ret)

# Append Mode
@app.route('/extract-child', methods=['POST'])
def extractChild():
    input_data = request.get_json(force=True)
    cmd = str(request.url_rule).replace("/","")
    ret = execute(cmd=cmd, input_data=input_data)
    return jsonify(ret)

# Append Mode
@app.route('/extract-parent', methods=['POST'])
def extractParent():
    input_data = request.get_json(force=True)
    cmd = str(request.url_rule).replace("/","")
    ret = execute(cmd=cmd, input_data=input_data)
    return jsonify(ret)

# Append Mode
@app.route('/extract-pos', methods=['POST'])
def extractPos():
    input_data = request.get_json(force=True)
    cmd = str(request.url_rule).replace("/","")
    ret = execute(cmd=cmd, input_data=input_data)
    return jsonify(ret)

# Append Mode
@app.route('/extract-dep', methods=['POST'])
def extractDep():
    input_data = request.get_json(force=True)
    cmd = str(request.url_rule).replace("/","")
    ret = execute(cmd=cmd, input_data=input_data)
    return jsonify(ret)

# Append Mode
@app.route('/extract-lemma', methods=['POST'])
def extractLemma():
    input_data = request.get_json(force=True)
    cmd = str(request.url_rule).replace("/","")
    ret = execute(cmd=cmd, input_data=input_data)
    return jsonify(ret)

# Append Mode
@app.route('/extract-by-rule-id', methods=['POST'])
def extractByRuleId():
    input_data = request.get_json(force=True)
    cmd = str(request.url_rule).replace("/","")
    ret = execute(cmd=cmd, input_data=input_data)
    return jsonify(ret)

# Append Mode
@app.route('/extract-child-of-token', methods=['POST'])
def extractChildOfToken():
    input_data = request.get_json(force=True)
    cmd = str(request.url_rule).replace("/","")
    ret = execute(cmd=cmd, input_data=input_data)
    return jsonify(ret)

# Append Mode
@app.route('/extract-parent-of-token', methods=['POST'])
def extractParentOfToken():
    input_data = request.get_json(force=True)
    cmd = str(request.url_rule).replace("/","")
    ret = execute(cmd=cmd, input_data=input_data)
    return jsonify(ret)

# Append Mode
@app.route('/extract-sibling-of-token', methods=['POST'])
def extractSiblingOfToken():
    input_data = request.get_json(force=True)
    cmd = str(request.url_rule).replace("/","")
    ret = execute(cmd=cmd, input_data=input_data)
    return jsonify(ret)

@app.route('/')
def index():
    return "Connection Succeeded"
    #return render_template("index.html")

def execute(cmd, input_data):
    global_logger.info("Starting {}".format(cmd))
    start_time = time.time()
    if 'org_field' in input_data:
        data = input_data['data']
        org_col_name = input_data['org_field']
        col_name = input_data['field']
        org_field_data = data[org_col_name]
        field_data = data[col_name]
        time_field_name = input_data['time_field']
        crawl_time = data[time_field_name]
    else:
        data = input_data['data']
        org_col_name = input_data['field']
        org_field_data = data[org_col_name]
        time_field_name = input_data['time_field']
        crawl_time = data[time_field_name]
   
    rule = input_data['rule'] if 'rule' in input_data else None
    pool = int(input_data['pool']) if 'pool' in input_data else None
    ent_dic = input_data['entity'] if 'entity' in input_data else None
    param_dic = input_data.copy()
    
    for key in ['cmd', 'org_field', 'field', 'data', 'rule', 'pool', 'entity', 'time_field']:
        param_dic.pop(key, None)

    loader.loadLoaderByEntity(ent_dic)
    loader.loadOrbCacheByRule(ent_dic, rule)
    
    org_field_dict = defaultdict(list)
    for idx, org_data in enumerate(org_field_data):
        org_field_dict[org_data].append(idx)

    new_text_list = []
    existed_doc = []
    for text, idx_list in org_field_dict.items():
        add_idx_list = []
        pickle_doc_list = []
        for idx in idx_list:
            pickle_doc = loader.getDocByKey(text, crawl_time[idx])
            if pickle_doc is None:
                add_idx_list.append(idx)
            pickle_doc_list.append(pickle_doc)
        if all(pickle_doc_list):
            existed_doc.append(pickle_doc_list[0])
        elif any(pickle_doc_list):
            pickle_tmp = next(pickle_doc for pickle_doc in pickle_doc_list if pickle_doc is not None)
            for idx in add_idx_list:
                loader.saveDocByKey(pickle_tmp, crawl_time[idx])
        else:
            new_text_list.append(text)

    new_text_uq = list(set(new_text_list))
    existed_doc_uq = list({v['org_text']:v for v in existed_doc}.values())
    
    global_logger.info("new_text:{}".format(len(new_text_uq)))
    global_logger.info("existed_text:{}".format(len(existed_doc_uq)))

    if len(new_text_uq) != 0:
        global_logger.info("Start Creating Spacy Doc Object ...")
        p_start_time = time.time()
        new_doc_uq = SpacyWrapper(new_text_uq, ent_dic, pool).default_sent
        for new_doc in new_doc_uq:
            new_text_idx = org_field_dict[new_doc['org_text']]
            for idx in new_text_idx:
                loader.saveDocByKey(new_doc, crawl_time[idx])
        total_doc_uq = existed_doc_uq.copy()
        total_doc_uq.extend(new_doc_uq)
        p_next_time = time.time() - p_start_time
        global_logger.info("Finished Creating Spacy Doc Object in {}...".format(round(p_next_time, 2)))
    else:
        global_logger.info("Not Creating Spacy Object ...")
        total_doc_uq = existed_doc_uq.copy()

    global_logger.info("Start Creating Orb Object ...")
    p_start_time = time.time()
    total_orb_list = []
    for doc in total_doc_uq:
        cached_orb = loader.getOrbByDoc(doc)
        if cached_orb:
            orb = cached_orb
        else:
            orb = Orb(doc, rule)
        loader.saveOrb(doc, orb)
        total_orb_list.append(orb)
    global_logger.info("Creates Orb in {}".format(round(time.time() - p_start_time, 2)))
    total_orb_dict = {}
    for orb in total_orb_list:
        orb_idx = org_field_dict[orb.org_text]
        for idx in orb_idx:
            total_orb_dict[idx] = orb
    total_orb_dict = OrderedDict(sorted(total_orb_dict.items()))
    p_next_time = time.time() - p_start_time
    global_logger.info("Finished Creating Orb Object in {}...".format(round(p_next_time, 2)))
   
    ret = [[org_col_name + cmd.replace("extract", "")]]
    start_ex_time = time.time()
    global_logger.info("Start Executing Command ...")
    for key, orb in total_orb_dict.items():
        if 'org_field' in input_data:
            field_kw = field_data[key]
            ret.append([orb.execute(cmd=cmd, target_content=field_kw, **param_dic)])
        else:
            ret.append([orb.execute(cmd=cmd, target_content=None, **param_dic)])
    next_ex_time = time.time() - start_ex_time
    global_logger.info("Finished Executing Command in {}...".format(round(next_ex_time, 2)))
    elapsed_time = time.time() - start_time
    global_logger.info("API Time : {}".format(round(elapsed_time, 2)))
    return ret

if __name__ == "__main__":
    host = global_config.getValue('COMMON', 'common.host')
    port = global_config.getValue('COMMON', 'common.port')
    app.run(host=host, port=port, debug=False)

