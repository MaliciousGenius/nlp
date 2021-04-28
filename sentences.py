#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from nltk.tokenize.punkt import PunktTrainer, PunktSentenceTokenizer


def create_sentences(text_file, min_sentence_len):
    trainer = PunktTrainer()
    trainer.INCLUDE_ALL_COLLOCS = True

    with open(text_file, "r") as input_file:
        paragraphs = input_file.read()

    trainer.train(paragraphs)

    tokenizer = PunktSentenceTokenizer(trainer.get_params())
    # print(tokenizer._params.abbrev_types)

    sentences = []

    for line in open(text_file, "r+").readlines():
        sentences_tmp = tokenizer.tokenize(line)
        for sentence in sentences_tmp:
            sentences.append(sentence)

    with open("dataset/sentences.txt", "a") as out_file:
        for sentence in sentences:
            if len(sentence) > min_sentence_len:
                out_file.write(sentence + "\n\n")

def main():
    if os.path.exists("dataset/sentences.txt"):
        os.remove("dataset/sentences.txt")

    create_sentences("dataset/paragraphs.txt", 150)

if __name__ == '__main__':
    main()


