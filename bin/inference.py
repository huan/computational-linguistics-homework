'''
doc
'''
import sys

import tensorflow as tf
import numpy as np

from chinese_segmentation.config import MAX_LEN
from chinese_segmentation.vocabulary import Vocabulary
from chinese_segmentation.model import build_model
from chinese_segmentation.data_loader import load_test_data

def main () -> int:
    with open('data/corpus_preprocessed.txt', 'r') as f:
        raw_text = f.read()

    voc = Vocabulary(raw_text)
    model = build_model(voc.size)

    X = load_test_data()
    X = voc.texts_to_padded_sequences(X)

    model.load_weights('./data/checkpoints/my_checkpoint')
    predicted = model.predict(X)

    result = np.ones(
        (
            predicted.shape[0],
            predicted.shape[1],
            predicted.shape[2],
        )
    ) * (predicted > 0.5)

    output(X, result, voc)


def output (X, y, voc):
    for n in range(X.shape[0]):
        # import pdb; pdb.set_trace()

        for t in range(X.shape[1]):
            idx = X[n, t]

            if idx == 0:
                continue

            zi = voc.tokenizer.index_word.get(idx)

            bi = y[n, t, 0]

            if bi == 1:
                sys.stdout.write(' ')

            sys.stdout.write(zi)

main()
