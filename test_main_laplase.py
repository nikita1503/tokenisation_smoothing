import numpy as np
from laplace_smoothing import laplace

info=np.load("info.dict.npy").item()
unigram = np.load("unigram.dict.npy").item()
bigram = np.load("bigram.dict.npy").item()
trigram = np.load("trigram.dict.npy").item()

l=laplace()
l.unigram_smooth(unigram,info["V"])
np.save("unigram_laplace.dict",l.unigram_laplace)

l.bigram_smooth(bigram,unigram,info["V"])
np.save("bigram_laplace.dict",l.bigram_laplace)

l.trigram_smooth(trigram,bigram,info["V"])
np.save("trigram_laplace.dict",l.trigram_laplace)
