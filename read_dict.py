import numpy as np

d=np.load("bigram_laplace_kn.dict.npy").item()
for x in d:
    print(x,d[x])
