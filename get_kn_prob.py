from __future__ import division

class kens
er_ney:
    def __init__(self):
        self.unigram_kn=dict()
        self.bigram_kn=dict()
        self.trigram_kn=dict()
        self.unigram=np.load("unigram.dict.npy").item()
        self.bigram=np.load("bigram.dict.npy").item()
        self.trigram=np.load("trigram.dict.npy").item()
        self.d=0.75
        self.n1w1=np.load("n1w1.dict.npy").item()
        self.n1w2=np.load("n1w2.dict.npy").item()
        self.n1w1w2=np.load("n1w1w2.dict.npy").item()
        self.n1w2w3=np.load("n1w2w3.dict.npy").item()
        self.info=np.load("info_kn.dict.npy").item()
        self.bigram_smooth=np.load("bigram_kn.dict.npy").item()
        self.trigram_smooth=np.load("trigram_kn.dict.npy").item()

    def get_kn_bigram(self,word1,word2):
        p=0
        if (word1,word2) in self.bigram_kn:
            p=self.bigram_kn[(word1,word2)]
        else:
            p=((self.d/self.unigram[ngram[0]])*self.n1w1[ngram[0]])*(self.n1w2[ngram[1]]/self.info["n1w2s"])
