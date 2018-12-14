import os

import pytest                   # type: ignore

from typing import (
    Iterable,
    List,
)

from .preprocess import (
    preprocess,
)

FILE_PATH = os.path.dirname(os.path.realpath(__file__))

CORPUS_FILE = os.path.join(FILE_PATH, '../tests/fixtures/199801_test.txt')
CORPUS_TEXT_FILE = os.path.join(FILE_PATH, '../tests/fixtures/199801_test_text.txt')
CORPUS_TAG_FILE = os.path.join(FILE_PATH, '../tests/fixtures/199801_test_tag.txt')

@pytest.fixture(scope='module')
def corpus_lines() -> Iterable[List[str]]:
    """ doc """
    with open(CORPUS_FILE, 'r') as f:
        yield f.readlines()


@pytest.fixture(scope='module')
def corpus_text_lines() -> Iterable[List[str]]:
    """ doc """
    with open(CORPUS_TEXT_FILE, 'r') as f:
        yield [
            line.strip()
            for line in f.readlines()
        ]


@pytest.fixture(scope='module')
def corpus_tag_lines() -> Iterable[List[str]]:
    """ doc """
    with open(CORPUS_TAG_FILE, 'r') as f:
        yield [
            line.strip()
            for line in f.readlines()
        ]


def test_preprocess(
        corpus_lines,
        corpus_text_lines,
        corpus_tag_lines,
) -> None:
    """ test """
    text_line_list, tag_line_list = preprocess(corpus_lines)

    # import pdb; pdb.set_trace()
    for i in range(len(corpus_lines)):
        assert text_line_list[i] == corpus_text_lines[i], 'should compute text right'
        assert tag_line_list[i] == corpus_tag_lines[i], 'should compute tag right'
