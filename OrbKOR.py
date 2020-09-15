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

    def __init__(self, rule=None):
        self.model_mgr = ModelMgr()

        if rule is None:
            rule = 'default'

        if OrbKOR.rule_mgr.rule != rule:
            OrbKOR.rule_mgr = RuleMgr(global_config, rule)

    def parse(self, data):
        self.clade_list = []
        if OrbKOR.parser.getSent(data):
            word_list = OrbKOR.parser.getSent(data).word_list
            self.clade_list = OrbKOR.rule_mgr.getClade(word_list)
        else:
            return "No Sentence"
