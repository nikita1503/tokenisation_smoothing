from __future__ import division
import numpy as np
class witten_bell:
    def __init__(self):
        self.info=np.load("info.dict.npy").item()
        self.unigram=np.load("unigram.dict.npy").item()
        self.bigram=np.load("bigram.dict.npy").item()
        self.trigram=np.load("trigram.dict.npy").item()
        self.n1w1=np.load("n1w1.dict.npy").item()
        self.n1w1w2=np.load("n1w1w2.dict.npy").item()
        self.unigram_wb=dict()
        self.bigram_wb=dict()
        self.trigram_wb=dict()

    def unigram_smooth(self):
        for word in self.unigram:
            self.unigram_wb[word]=(self.info["chEp"]/(self.info["chEp"]+self.info["n1Ep"]))*(self.unigram[word]/self.info["chEp"])

    def bigram_smooth(self):
        for ngram in self.bigram:
            self.bigram_wb[ngram]=(self.unigram[ngram[0]]/(self.unigram[ngram[0]]+self.n1w1[ngram[0]]))*(self.bigram[ngram]/self.unigram[ngram[0]]) + (self.n1w1[ngram[0]]/(self.unigram[ngram[0]]+self.n1w1[ngram[0]]))*self.unigram_wb[ngram[0]]

    def trigram_smooth(self):
        for ngram in self.trigram:
            tup=(ngram[0],ngram[1]);
            self.trigram_wb[ngram]=(self.bigram[tup]/(self.bigram[tup]+self.n1w1w2[tup]))*(self.trigram[ngram]/self.bigram[tup]) + (self.n1w1w2[tup]/(self.bigram[tup]+self.n1w1w2[tup]))*self.bigram_wb[(ngram[0],ngram[1])]
