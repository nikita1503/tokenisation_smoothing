from __future__ import division
import numpy as np

class laplace:
    def __init__(self):
        self.info=np.load("info.dict.npy").item()
        self.unigram = np.load("unigram.dict.npy").item()
        self.bigram = np.load("bigram.dict.npy").item()
        self.trigram = np.load("trigram.dict.npy").item()
        self.unigram_smooth = np.load("unigram_laplace.dict.npy").item()
        self.bigram_smooth = np.load("bigram.dict.npy").item()
        self.trigram_smooth = np.load("trigram.dict.npy").item()
        self.N=len(self.unigram)

    def get_laplace_unigram(self,word):
        p=0
        if word not in self.unigram_smooth:
            p=1/(self.N+self.info["V"])
        else:
            p=self.unigram_smooth[word]
        return p

    def get_laplace_bigram(self,word1,word2):
        p=0
        if (word1,word2) not in self.bigram_smooth:
            if word1 not in self.unigram_smooth:
                p=1/self.info["V"]
            else:
                p=1/(self.unigram[word1]+self.info["V"])
        else:
            p=self.bigram_smooth[(word1,word2)]
        return p

    def get_laplace_trigram(self,word1,word2,word3):
        p=0
        if (word1,word2,word3) not in self.trigram_smooth:
            if (word1,word2) not in self.bigram_smooth:
                p=1/self.info["V"]
            else:
                p=1/(self.bigram[(word1,word2)]+self.info["V"])
        else:
            p=self.trigram_smooth[(word1,word2,word3)]

        return p
