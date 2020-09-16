from orbKOR.util.parse.Word import Word

class Sent:
    def __init__(self, data):
        self.sent = data['form']
        self.word_list = []
        self.root = None

        for d in data['DP']:
            word = Word(idx=d['word_id'], txt=d['word_form'], dp=d['label'])
            self.word_list.append(word)

        for data, word in zip(data['DP'], self.word_list):
            if data['head'] != -1:
                head_word = self.getWordById(data['head'])
                word.head = head_word
                head_word.children.append(word)
            else:
                word.head = 'ROOT'
        
        for word in self.word_list:
            if word.head == 'ROOT':
                self.root = word

    def getWordById(self, idx):
        for word in self.word_list:
            if word.idx == idx:
                return word
       
