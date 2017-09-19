from __future__ import division
import numpy as np
class kenser_ney:
    def __init__(self):
        self.bigram_kn=dict()
        self.trigram_kn=dict()
        self.bigram_laplace_kn=dict()
        self.trigram_laplace_kn=dict()
        self.bigram_wb_kn=dict()
        self.trigram_wb_kn=dict()
        self.unigram=np.load("unigram.dict.npy").item()
        self.bigram=np.load("bigram.dict.npy").item()
        self.trigram=np.load("trigram.dict.npy").item()
        self.d=0.75
        self.n1w1=np.load("n1w1.dict.npy").item()
        self.n1w2=np.load("n1w2.dict.npy").item()
        self.n1w1w2=np.load("n1w1w2.dict.npy").item()
        self.n1w2w3=np.load("n1w2w3.dict.npy").item()
        self.info=np.load("info.dict.npy").item()
        self.bigram_laplace=np.load("bigram_laplace.dict.npy").item()
        self.trigram_laplace=np.load("trigram_laplace.dict.npy").item()
        self.bigram_wb=np.load("bigram_wb.dict.npy").item()
        self.trigram_wb=np.load("trigram_wb.dict.npy").item()

    def bigram_smooth(self):
        for ngram in self.bigram:
            self.bigram_kn[ngram]=(max(self.bigram[ngram]-self.d,0)/self.unigram[ngram[0]])+((self.d/self.unigram[ngram[0]])*self.n1w1[ngram[0]])*(self.n1w2[ngram[1]]/self.info["n1w2s"])

    def trigram_smooth(self):
        nbt=len(self.bigram)
        for ngram in self.trigram:
            tup=(ngram[0],ngram[1])
            tup1=(ngram[1],ngram[2])
            self.trigram_kn[ngram]=(max(self.trigram[ngram]-self.d,0)/self.bigram[tup]) + self.d*(self.n1w1w2[tup]/self.bigram[tup])*((max(self.n1w2w3[tup1]-self.d,0)/self.n1w2[ngram[1]]) + self.d*(self.n1w1[ngram[1]]/self.n1w2[ngram[1]])*(self.n1w2[ngram[2]]/nbt))

    def bigram_smooth_laplace_kn(self):
        for ngram in self.bigram_laplace:
            self.bigram_laplace_kn[ngram]=(max((self.bigram_laplace[ngram]*self.unigram[ngram[0]])-self.d,0)/self.unigram[ngram[0]])+((self.d/self.unigram[ngram[0]])*self.n1w1[ngram[0]])*(self.n1w2[ngram[1]]/self.info["n1w2s"])

    def trigram_smooth_laplace_kn(self):
        nbt=len(self.bigram_laplace)
        for ngram in self.trigram_laplace:
            tup=(ngram[0],ngram[1])
            tup1=(ngram[1],ngram[2])
            self.trigram_laplace_kn[ngram]=(max((self.trigram_laplace[ngram]*self.bigram[tup])-self.d,0)/self.bigram[tup]) + self.d*(self.n1w1w2[tup]/self.bigram[tup])*((max(self.n1w2w3[tup1]-self.d,0)/self.n1w2[ngram[1]]) + self.d*(self.n1w1[ngram[1]]/self.n1w2[ngram[1]])*(self.n1w2[ngram[2]]/nbt))

    def bigram_smooth_wb_kn(self):
        for ngram in self.bigram_wb:
            self.bigram_wb_kn[ngram]=(max((self.bigram_wb[ngram]*self.unigram[ngram[0]])-self.d,0)/self.unigram[ngram[0]])+((self.d/self.unigram[ngram[0]])*self.n1w1[ngram[0]])*(self.n1w2[ngram[1]]/self.info["n1w2s"])

    def trigram_smooth_wb_kn(self):
        nbt=len(self.bigram_laplace)
        for ngram in self.trigram_wb:
            tup=(ngram[0],ngram[1])
            tup1=(ngram[1],ngram[2])
            self.trigram_wb_kn[ngram]=(max((self.trigram_wb[ngram]*self.bigram[tup])-self.d,0)/self.bigram[tup]) + self.d*(self.n1w1w2[tup]/self.bigram[tup])*((max(self.n1w2w3[tup1]-self.d,0)/self.n1w2[ngram[1]]) + self.d*(self.n1w1[ngram[1]]/self.n1w2[ngram[1]])*(self.n1w2[ngram[2]]/nbt))
