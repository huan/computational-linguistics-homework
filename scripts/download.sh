#!/usr/bin/env bash

[ -d data/ ] || mkdir data

curl -L -o data/199801.txt https://github.com/hankcs/OpenCorpus/raw/master/pku98/199801.txt
curl -L -o data/bigram_test.txt https://github.com/824zzy/blogResources/raw/master/txtRestources/bigram_test.txt

iconv -f gbk -t utf-8 < data/bigram_test.txt > data/bigram_test.utf8.txt
mv data/bigram_test.utf8.txt data/bigram_test.txt
