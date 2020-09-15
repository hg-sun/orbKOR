import json

from util.parse.Doc import Doc

class Parser:
    def __init__(self, config):
        input_path = config.getValue('Parser', 'input.json.file')
        self.doc_list = []

        with open(input_path, 'rb') as f:
            data = json.load(f)

        for d in data['document']:
            doc = Doc(d)
            self.doc_list.append(doc)

    def checkSent(self, data):
        check = False
        for doc in self.doc_list:
            for sent in doc.sent_list:
                if sent == data:
                    check = True
        return check
