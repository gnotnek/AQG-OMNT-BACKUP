import nltk
from nlp_id.postag import PosTag
from nlp_id.tokenizer import Tokenizer 

nltk.download('punkt')

tokenizer = Tokenizer() 
postagger = PosTag() 

def tokenize(s):
    tokenizer.tokenize(s)
    return s

def get_pos_tag(text):
    tags = postagger.get_pos_tag(text)
    sentences = [[]]

    for item in tags:
        # word = item[0]
        tag = item[1]

        sentences[-1].append(item)

        if tag == 'PUN':
            sentences.append([])

    print(sentences)
    return {'postags':sentences}