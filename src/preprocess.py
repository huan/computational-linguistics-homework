import os
import re

BEGIN = 'B'
INNER = 'I'

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

            line_text = line_text + word_text + ' '
            line_tag = line_tag + word_tag + ' '

        line_text_list.append(line_text.strip())
        line_tag_list.append(line_tag.strip())

    return line_text_list, line_tag_list


def main () -> int:
    FILE_PATH = os.path.dirname(os.path.realpath(__file__))
    DATA_FILE = os.path.join(FILE_PATH, '../data/199801.txt')

    with open(DATA_FILE) as file:
        line_list = file.readlines()

    text_list, tag_list = preprocess(line_list)

    for text, tag in zip(text_list, tag_list):
        print('{}\t{}'.format(text, tag))


if __name__ == "__main__":
    main()
