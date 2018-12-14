import os

from chinese_segmentation.preprocess import preprocess

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
