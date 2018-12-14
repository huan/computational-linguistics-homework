import os
import re

BEGIN = '1'
INNER = '0'

from .config import (
    MAX_LEN,
)

def preprocess(line_list):

    line_text_list = []
    line_tag_list = []

    for line in line_list:
        # import pdb; pdb.set_trace()
        line = line.strip()
        line_text = ''
        line_tag = ''

        word_list = [
            word
            for word in re.split(r'/[^\s]+\s*', line)
        ]
        # import pdb; pdb.set_trace()

        for word_text in word_list:
            if len(word_text) == 0:
                continue
            word_tag = BEGIN + INNER * ( len(word_text) - 1 )

            line_text = line_text + word_text
            line_tag = line_tag + word_tag

            if word_text == '。' or len(line_text) + 10 >= MAX_LEN:
                line_text_list.append(line_text.strip())
                line_tag_list.append(line_tag.strip())
                line_text = ''
                line_tag = ''

        if len(line_text) > 0:
            line_text_list.append(line_text.strip())
            line_tag_list.append(line_tag.strip())

    return line_text_list, line_tag_list
