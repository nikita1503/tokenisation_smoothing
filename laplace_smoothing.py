from __future__ import division
class laplace:
    def unigram_smooth(self,unigram,V):
        self.unigram_laplace=dict()
        self.N=len(unigram)
        for word in unigram:
            self.unigram_laplace[word]=((unigram[word]+1))/(self.N+V)
            #print(word,self.unigram_laplace[word])

    def bigram_smooth(self,bigram, unigram, V):
        self.bigram_laplace=dict()
        for ngram in bigram:
            self.bigram_laplace[ngram]=((bigram[ngram]+1))/(unigram[ngram[0]]+V)
            #print(ngram,self.bigram_laplace[ngram])

    def trigram_smooth(self,trigram, bigram, V):
        self.trigram_laplace=dict()
        for ngram in trigram:
            self.trigram_laplace[ngram]=((trigram[ngram]+1))/(bigram[ngram[:2]]+V)
            #print(ngram,self.tigram_laplace[ngram[:1]])
