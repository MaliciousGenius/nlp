#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import nltk

def check_if_string_in_file(file_name, string_to_search):
    with open(file_name, 'r+') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
    return False

def create_paragraphs(dataset_type):

    if os.path.exists("paragraphs." + dataset_type):
        os.remove("paragraphs." + dataset_type)

    paragraphs = []

    for text_file in os.scandir("dataset/text_files"):
        if text_file.is_file() and text_file.path.split('.')[-1].lower() == dataset_type:
            for line in open(text_file, "r+").readlines():
                line = line.strip()
                if len(line) > 3 and line[0].isupper() and line[-1] == '.':
                    paragraphs.append(line)

    with open("paragraphs." + dataset_type, "a") as out:
        for paragraph in paragraphs:
            out.write(paragraph + "\n")

def distillation_paragraphs(dataset_type, min_paragraph_len):
    if not os.path.exists("paragraphs.txt"):
        with open("paragraphs.txt", "w"):
            pass
    for line in open("paragraphs." + dataset_type, "r").readlines():
        if not check_if_string_in_file("paragraphs.txt", line):
            if len(line) > min_paragraph_len:
                with open("paragraphs.txt", "a") as out:
                    out.write(line)


def main():
    create_paragraphs("summary")
    create_paragraphs("text")

    if os.path.exists("paragraphs.txt"):
        os.remove("paragraphs.txt")

    distillation_paragraphs("summary", 100)
    distillation_paragraphs("text", 500)

    if os.path.exists("paragraphs.summary"):
        os.remove("paragraphs.summary")

    if os.path.exists("paragraphs.text"):
        os.remove("paragraphs.text")

if __name__ == '__main__':
    main()

# for text_file in os.scandir("dataset/text_files"):
#     if text_file.is_file() and text_file.path.split('.')[-1].lower() == "summary":
#         for line in open(text_file, "r+").readlines():
#             sentences_temp = nltk.sent_tokenize(line)
#             for sentence in sentences_temp:
#                 print(sentence)
#                 print('-S------')
#             print('-L------')
#         print('-T------')
