'''
data loader
'''
import gzip
import re
from typing import (
    # Any,
    List,
    Tuple,
)

import tensorflow as tf
import numpy as np

from .config import (
    MAX_LEN,
)


def load_data ():
    '''doc'''
    with open('data/corpus_preprocessed.txt', 'r') as f:
        line_list = f.readlines()

    X = []
    y = np.zeros((
        len(line_list),
        MAX_LEN,
        1,
    ))

    # import pdb; pdb.set_trace()

    for i, line in enumerate(line_list):

        # if i % 100 == 0:
        #     print ('loading data ... {}'.format(i))

        text, tag = re.split(r'\t', line.strip())

        X.append(list(text))

        for bi_idx, bi_char in enumerate(tag):
            y[i, bi_idx, 0] = float(bi_char)

    return X, y


def load_test_data ():
    '''doc'''
    with open('data/bigram_test.txt', 'r') as f:
        line_list = f.readlines()

    X = []

    for line in line_list:
        line = line.strip()
        for text in line.split('。'):
            X.append(list(text))

    return X
