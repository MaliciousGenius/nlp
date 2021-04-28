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

    if os.path.exists("dataset/paragraphs." + dataset_type):
        os.remove("dataset/paragraphs." + dataset_type)

    paragraphs = []

    for text_file in os.scandir("dataset/text_files"):
        if text_file.is_file() and text_file.path.split('.')[-1].lower() == dataset_type:
            for line in open(text_file, "r+").readlines():
                line = line.strip()
                if len(line) > 3 and line[0].isupper() and line[-1] == '.':
                    paragraphs.append(line)

    with open("dataset/paragraphs." + dataset_type, "a") as out:
        for paragraph in paragraphs:
            out.write(paragraph + "\n")

def distillation_paragraphs(dataset_type, min_paragraph_len, max_paragraph_len):
    if not os.path.exists("dataset/paragraphs.txt"):
        with open("dataset/paragraphs.txt", "w"):
            pass
    for line in open("dataset/paragraphs." + dataset_type, "r").readlines():
        if not check_if_string_in_file("dataset/paragraphs.txt", line):
            if len(line) > min_paragraph_len and len(line) < max_paragraph_len and line.count('.') < 10 and line.count('ISBN') == 0:
                with open("dataset/paragraphs.txt", "a") as out:
                    out.write(line + "\n")


def main():
    create_paragraphs("summary")
    create_paragraphs("text")

    if os.path.exists("dataset/paragraphs.txt"):
        os.remove("dataset/paragraphs.txt")

    distillation_paragraphs("summary", 50, 3000)
    distillation_paragraphs("text", 200, 3000)

    if os.path.exists("dataset/paragraphs.summary"):
        os.remove("dataset/paragraphs.summary")

    if os.path.exists("dataset/paragraphs.text"):
        os.remove("dataset/paragraphs.text")

if __name__ == '__main__':
    main()

