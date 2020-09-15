from util.parse.Sent import Sent

class Doc:
    def __init__(self, data):
        self.sent_list = []
        
        for d in data['sentence']:
            sent = Sent(d)
            self.sent_list.append(sent)

