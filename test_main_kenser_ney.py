from tokenise_kn import tokenise
from kenser_ney import kenser_ney
import numpy as np
"""corpus=raw_input("Enter the name of corpus file: ")
V=int(raw_input("Enter size of vocabulary: "))
t=tokenise(corpus)
t.unigram_create()
np.save("unigram.dict",t.unigram)
t.bigram_create()
info={'corpus':corpus,'V':V, "chEp":t.chEp, "n1Ep":t.n1Ep, "n1w2s":t.n1w2s}
np.save("info_kn.dict",info)
np.save("n1w1.dict",t.n1w1)
np.save("n1w2.dict",t.n1w2)
np.save("bigram.dict",t.bigram)
t.trigram_create()
np.save("n1w1w2.dict",t.n1w1w2)
np.save("n1w2w3.dict",t.n1w2w3)
np.save("trigram.dict",t.trigram)"""

w=kenser_ney()
w.bigram_smooth()
np.save("bigram_kn.dict",w.bigram_kn)
w.trigram_smooth()
np.save("trigram_kn.dict",w.trigram_kn)
w.bigram_smooth_laplace_kn()
np.save("bigram_laplace_kn.dict",w.bigram_laplace_kn)
w.trigram_smooth_laplace_kn()
np.save("trigram_laplace_kn.dict",w.trigram_laplace_kn)
w.bigram_smooth_wb_kn()
np.save("bigram_wb_kn.dict",w.bigram_wb_kn)
w.trigram_smooth_wb_kn()
np.save("trigram_wb_kn.dict",w.trigram_wb_kn)
