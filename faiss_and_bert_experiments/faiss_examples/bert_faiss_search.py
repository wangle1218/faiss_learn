# coding: utf-8
from gensim.models.doc2vec import Doc2Vec
import numpy as np
import faiss
import sys

if __name__ == "__main__":
    doc_num = int(sys.argv[1])
        
    with open("postlist.txt") as f:
        data = [line.strip() for line in f]

    print("[target doc:", data[doc_num], "]\n")
    index = faiss.read_index("./faiss_bert.faiss")
    vec = index.reconstruct(doc_num)
    D,I = index.search(np.array([vec]), k=30)
    for i in I[0]:
        print(data[i])
