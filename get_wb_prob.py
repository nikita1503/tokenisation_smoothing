from __future__ import division
import numpy as np
class witten_bell:
    self.info=np.load("info_wb.dict").item()
    self.unigram=np.load("unigram.dict").item()
    self.bigram=np.load("bigram.dict").item()
    self.trigram=np.load("trigram.dict").item()
    self.unigram_smooth=np.load("unigram_wb.dict").item()
    self.bigram_smooth=np.load("bigram_wb.dict").item()
    self.trigram_smooth=np.load("trigram_wb.dict").item()
    def witten_bell_unigram(self,word):
        p=0
        if word not in self.unigram_smooth:
            p=(info("n1Ep")/(info["chEp"]+info["n1Ep"]))/info["V"]

        else:
            p=unigram_smooth[word]

        return p

    def witten_bell_bigram(self,word1,word2):
        p=0
        if (word1,word2) not in self.bigram_smooth:
            if word1 not in self.unigram_smooth:
                p=self.witten_bell_unigram(word1)
            else:
                p=(self.n1w[word1]/(self.unigram[word1]+self.n1w[word1]))*self.witten_bell_unigram(word1)
        else:
            p=self.bigram_smooth[(word1,word2)]
        return p

    def witten_bell_trigram(self,word1,word2,word3):
        p=0
        if (word1,word2,word3) not in self.trigram_smooth:
            if (word1,word2) not in self.bigram_smooth:
                p=self.witten_bell_bigram(word1,word2)
            else:
                p=(n1w1w2[(word1,word2)]/(self.bigram[(word1,word2)]+n1w1w2[(word1,word2)]))*self.witten_bell_bigram(word1,word2)
        else:
            p=self.trigram_smooth[(word1,word2,word3)]
        return p
