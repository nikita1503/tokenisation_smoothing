class process_tokens:
    def __init__(self,corpus):
        fp=open(corpus,"r")
        for line in fp:
            line=line.split(" ")
            for word in line:
