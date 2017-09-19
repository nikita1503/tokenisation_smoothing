import numpy as np
class prediction:
    def __init__(self):
        self.bigram_kn=np.load("bigram_kn.dict.npy").item()
        self.trigram_kn=np.load("trigram_kn.dict.npy").item()
    def bigram_predict(self):
        word="#"
        text_predicted=""
        used_bigram=[]
        written=False
        while(word != "%"):
            next_ngram=""
            maxp=-1
            for ngram in self.bigram_kn:
                if ngram[0]==word and ngram not in used_bigram:
                    if self.bigram_kn[ngram] > maxp:
                        if ngram[1]!="%" or written:
                            maxp=self.bigram_kn[ngram]
                            next_ngram=ngram
            word=next_ngram[1]
            if(word!="%"):
                text_predicted+=" "+word
                written=True
                used_bigram.append(next_ngram)
        #print(text_predicted)
        fp=open("predict_bigram","w")
        fp.write(text_predicted)
        fp.close()

    def trigram_predict(self):
        maxp=-1
        for ngram in self.bigram_kn:
            if ngram[0]=="#":
                if self.bigram_kn[ngram] > maxp:
                    if ngram[1]!="%":
                        maxp=self.bigram_kn[ngram]
                        word=ngram[1]

        text_predicted=word+" "
        bgram=("#",word);
        used_trigram=[]
        while(word!="%"):
            maxp=-1
            for ngram in self.trigram_kn:
                if (ngram[0],ngram[1])==bgram and ngram not in used_trigram:
                    if self.trigram_kn[ngram] > maxp:
                        maxp=self.trigram_kn[ngram]
                        word=ngram[2]
            if(word!="%"):
                text_predicted+=word+" "
                used_trigram.append((bgram[0],bgram[1],word))
            bgram=(bgram[1],word);
            #print(word)
        fp=open("predict_trigram","w")
        fp.write(text_predicted)
        fp.close()

p=prediction()
p.bigram_predict()
p.trigram_predict()
