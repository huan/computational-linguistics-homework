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
    y = np.array([]).reshape(0, MAX_LEN, 1)

    for line in line_list:
        text, tag = re.split(r'\t', line)

        text = re.sub(r'\s*', '', text).strip()
        tag = re.sub(r'\s*', '', tag).strip()
        tag = tag + ( '0' * ( MAX_LEN - len(tag) ) )

        # import pdb; pdb.set_trace()

        tag = np.array([
            float(char)
            for char in tag
        ]).reshape(1, MAX_LEN, 1)

        X.append(list(text))
        y = np.append(y, tag, axis=0)

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
