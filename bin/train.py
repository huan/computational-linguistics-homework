'''
doc
'''
import os

import tensorflow as tf
import numpy as np

from chinese_segmentation.config import MAX_LEN
from chinese_segmentation.vocabulary import Vocabulary
from chinese_segmentation.model import build_model
from chinese_segmentation.data_loader import load_data

FILE_PATH = os.path.dirname(os.path.realpath(__file__))
CHECKPOINT_PATH = os.path.join(FILE_PATH, '../data/checkpoints/')
CHECKPOINT_FILE = os.path.join(CHECKPOINT_PATH, 'my_checkpoint')

def main () -> int:
    with open('data/corpus_preprocessed.txt', 'r') as f:
        raw_text = f.read()

    voc = Vocabulary(raw_text)
    model = build_model(voc.size)

    X, y = load_data()
    X = voc.texts_to_padded_sequences(X)


    if os.path.exists(CHECKPOINT_PATH):
        model.load_weights(CHECKPOINT_FILE)
        print('Checkponit loaded.')
    else:
        print('No checkponit fount.')

    model.summary()

    model.fit(X, y, batch_size=128, epochs=5)
    model.save_weights(CHECKPOINT_FILE)

    # predicted = model.predict(X[0:3])
    # result = np.ones(
    #     (
    #         predicted.shape[0],
    #         predicted.shape[1],
    #         predicted.shape[2],
    #     )
    # ) * (predicted > 0.5)
    # print(result)
    # print('-'*80)
    # print(y[0:3])
    # print('-'*80)
    # import pdb; pdb.set_trace()

    # a = result - y[0:3]
    # b = np.mean(a)

main()
