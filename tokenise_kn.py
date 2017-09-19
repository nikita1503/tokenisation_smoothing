from __future__ import division
import re
class tokenise:
    def __init__(self,corpus):
        self.unigram=dict()
        self.bigram=dict()
        self.trigram=dict()
        self.remove_dets = [",", ".", "*", "'", '"', "/", "!", "=", "[","]", "(",")", "{","}", "@", "#", "$", "%", "^", "-", "_", ":", ";", "?", "\\", "|", "<", ">", "~"] # define desired replacements here
        self.corpus_file=corpus
        #self.unigram_create()
    def unigram_create(self):
        fp=open(self.corpus_file,"r")
        self.chEp=0
        self.n1Ep=0
        for l in fp:
            l=re.split(" |\n|\t",l)
            for w in l:
                for d in self.remove_dets:
                    w=w.replace(d,"")
                if w in self.unigram:
                    self.unigram[w]+=1
                    self.chEp+=1
                else:
                    self.unigram[w]=1
                    self.chEp+=1
                    self.n1Ep+=1
        #for w in self.unigram:
        #    print(w,self.unigram[w])

    def bigram_create(self):
        fp=open(self.corpus_file,"r")
        self.n1w1=dict()
        self.n1w2=dict()
        self.n1w2s=0
        prev_word="$"
        for sent in fp:
            sent=re.split("\. ",sent)
            for l in sent:
                prev_word=""
                first_word = True
                l=re.split(" |\n|\t",l)
                for w in l:
                    for d in self.remove_dets:
                        w=w.replace(d,"")
                    if(w):
                        tup=(prev_word,w);
                        if tup in self.bigram:
                            self.bigram[tup]+=1
                        else:
                            self.bigram[tup]=1
                            if prev_word in self.n1w1:
                                self.n1w1[prev_word]+=1
                            else:
                                self.n1w1[prev_word]=1
                            if w in self.n1w2:
                                self.n1w2[w]+=1
                            else:
                                self.n1w2[w]=1
                            self.n1w2s+=1
                    if(w):
                        prev_word=w
        #for w in self.bigram:
        #    print(w,self.bigram[w])

    def trigram_create(self):
        fp=open(self.corpus_file,"r")
        self.n1w1w2=dict()
        self.n1w2w3=dict()
        for sent in fp:
            sent=re.split("\. ",sent)
            for l in sent:
                prev_word1=""
                prev_word2=""
                first_word = True
                second_word = True
                l=re.split(" |\n|\t",l)
                for w in l:
                    for d in self.remove_dets:
                        w=w.replace(d,"")
                    if(w):
                        if first_word:
                            first_word=False
                        else:
                            tup=(prev_word1,prev_word2,w);
                            tup1=(prev_word1,prev_word2);
                            tup2=(prev_word2,w);
                            if tup in self.trigram:
                                self.trigram[tup]+=1
                            else:
                                self.trigram[tup]=1
                                if tup1 in self.n1w1w2:
                                    self.n1w1w2[tup1]+=1
                                else:
                                    self.n1w1w2[tup1]=1
                                if tup2 in self.n1w2w3:
                                    self.n1w2w3[tup2]+=1
                                else:
                                    self.n1w2w3[tup2]=1
                    if(w):
                        prev_word1=prev_word2
                        prev_word2=w

        #for w in self.trigram:
        #    print(w,self.trigram[w])
