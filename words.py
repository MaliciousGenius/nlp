#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from nltk.tokenize import word_tokenize

# нужна функция которая в качестве аргумента принимает две строки символов
# первая строка - слово
# вторая строка - алфавит
# результат функции булево значение принадлежности к алфавиту


def check_if_string_in_file(file_name, string_to_search):
    with open(file_name, 'r+') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
    return False

def create_words(text_file):
    if not os.path.exists("dataset/words.txt"):
        with open("dataset/words.txt", "w"):
            pass

    words = []

    for line in open(text_file, "r+").readlines():
        words_tmp = word_tokenize(line)
        for word in words_tmp:
            if word.isalpha():
                words.append(word)

    for word in words:
        word_lower = word.lower()
        if not check_if_string_in_file("dataset/words.txt", word_lower):
            with open("dataset/words.txt", "a") as out_file:
                out_file.write(word_lower + "\n")

def main():
    if os.path.exists("dataset/words.txt"):
        os.remove("dataset/words.txt")

    create_words("dataset/sentences.txt")

if __name__ == '__main__':
    main()
