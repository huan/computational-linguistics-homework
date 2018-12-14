import pytest

from .data_loader import (
    load_data,
)

def test_load_data ():
    X, y = load_data()
    # import pdb; pdb.set_trace()
    assert len(X) == len(y), 'len(x) == len(y)'
    for i in range(len(X)):
        assert len(X[i]) == len(y[i]), 'len(x[i]) == len(y[i])'
