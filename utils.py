import numpy as np


class2label = {'Other': 0,
               'Message-Topic(e1,e2)': 1, 'Message-Topic(e2,e1)': 2,
               'Product-Producer(e1,e2)': 3, 'Product-Producer(e2,e1)': 4,
               'Instrument-Agency(e1,e2)': 5, 'Instrument-Agency(e2,e1)': 6,
               'Entity-Destination(e1,e2)': 7, 'Entity-Destination(e2,e1)': 8,
               'Cause-Effect(e1,e2)': 9, 'Cause-Effect(e2,e1)': 10,
               'Component-Whole(e1,e2)': 11, 'Component-Whole(e2,e1)': 12,
               'Entity-Origin(e1,e2)': 13, 'Entity-Origin(e2,e1)': 14,
               'Member-Collection(e1,e2)': 15, 'Member-Collection(e2,e1)': 16,
               'Content-Container(e1,e2)': 17, 'Content-Container(e2,e1)': 18}

label2class = {0: 'Other',
               1: 'Message-Topic(e1,e2)', 2: 'Message-Topic(e2,e1)',
               3: 'Product-Producer(e1,e2)', 4: 'Product-Producer(e2,e1)',
               5: 'Instrument-Agency(e1,e2)', 6: 'Instrument-Agency(e2,e1)',
               7: 'Entity-Destination(e1,e2)', 8: 'Entity-Destination(e2,e1)',
               9: 'Cause-Effect(e1,e2)', 10: 'Cause-Effect(e2,e1)',
               11: 'Component-Whole(e1,e2)', 12: 'Component-Whole(e2,e1)',
               13: 'Entity-Origin(e1,e2)', 14: 'Entity-Origin(e2,e1)',
               15: 'Member-Collection(e1,e2)', 16: 'Member-Collection(e2,e1)',
               17: 'Content-Container(e1,e2)', 18: 'Content-Container(e2,e1)'}

class2label_short = {
               'Cause-Effect(e1,e2)': 0, 'Cause-Effect(e2,e1)': 1,
               'Component-Whole(e1,e2)': 2, 'Component-Whole(e2,e1)': 3,
               'Entity-Origin(e1,e2)': 4, 'Entity-Origin(e2,e1)': 5,
               'Member-Collection(e1,e2)': 6, 'Member-Collection(e2,e1)': 7,
               'Content-Container(e1,e2)': 8, 'Content-Container(e2,e1)': 9}

class2labelT = {'HAS_CAUSE(e1,e2)': 0, 'HAS_CAUSE(e2,e1)': 1,
                'HAS_RESULT(e1,e2)': 2, 'HAS_RESULT(e2,e1)': 3,
                'HAS_FORM(e1,e2)': 4, 'HAS_FORM(e2,e1)': 5,
                'HAS_LOCATION(e1,e2)': 6, 'HAS_LOCATION(e2,e1)': 7,
                'HAS_ATTRIBUTE(e1,e2)': 8, 'HAS_ATTRIBUTE(e2,e1)': 9,
                'DEFINED_AS(e1,e2)': 10, 'DEFINED_AS(e2,e1)': 11,}

label2classT = {0: 'HAS_CAUSE(e1,e2)', 1: 'HAS_CAUSE(e2,e1)',
                2: 'HAS_RESULT(e1,e2)', 3: 'HAS_RESULT(e2,e1)',
                4: 'HAS_FORM(e1,e2)', 5: 'HAS_FORM(e2,e1)',
                6: 'HAS_LOCATION(e1,e2)', 7: 'HAS_LOCATION(e2,e1)',
                8: 'HAS_ATTRIBUTE(e1,e2)', 9: 'HAS_ATTRIBUTE(e2,e1)',
                10: 'DEFINED_AS(e1,e2)', 11: 'DEFINED_AS(e2,e1)'}


def load_glove(embedding_path, embedding_dim, vocab):
    # initial matrix with random uniform
    initW = np.random.randn(len(vocab.vocabulary_), embedding_dim).astype(np.float32) / np.sqrt(len(vocab.vocabulary_))
    # load any vectors from the word2vec
    print("Load glove file {0}".format(embedding_path))
    f = open(embedding_path, 'r', encoding='utf8')
    for line in f:
        splitLine = line.split(' ')
        word = splitLine[0]
        embedding = np.asarray(splitLine[1:], dtype='float32')
        idx = vocab.vocabulary_.get(word)
        if idx != 0:
            initW[idx] = embedding
    return initW
