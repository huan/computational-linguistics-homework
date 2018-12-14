'''
doc
'''
import tensorflow as tf
import numpy as np

from chinese_segmentation.config import MAX_LEN
from chinese_segmentation.vocabulary import Vocabulary
from chinese_segmentation.model import build_model
from chinese_segmentation.data_loader import load_data

def main () -> int:
    with open('data/corpus_preprocessed.txt', 'r') as f:
        raw_text = f.read()

    voc = Vocabulary(raw_text)
    model = build_model(voc.size)

    X, y = load_data()
    X = voc.texts_to_padded_sequences(X)

    model.fit(X, y, batch_size=16, epochs=1)

    predicted = model(X[0:3])
    print(predicted)
    print('-'*100)
    print(y[0:3])

main()
