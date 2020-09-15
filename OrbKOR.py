import os, sys

from ConfigMgr import ConfigMgr
from RuleMgr import RuleMgr
from ModelMgr import ModelMgr
from util.parse.Parser import Parser

current_path = os.path.dirname(os.path.abspath(__file__))
global_config = ConfigMgr(current_path)
parser = None

class OrbKOR:
    parser = Parser(global_config)
    rule_mgr = RuleMgr(global_config, rule=None)

    def __init__(self, data, rule=None):
        self.model_mgr = ModelMgr()

        if rule is None:
            rule = 'default'

        if OrbKOR.rule_mgr.rule != rule:
            OrbKOR.rule_mgr = RuleMgr(global_config, rule)

        if parser.getSent(data):
            return True
        else:
            return "No Sentence"
    
