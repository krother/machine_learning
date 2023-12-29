
import numpy as np

def cosine_similarity(a, b):
    """Returns cosine similarity of two word vectors"""
    return a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
