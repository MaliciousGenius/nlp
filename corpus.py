#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import nltk
# nltk.download('inaugural')
import os


from nltk.corpus import inaugural


corpus_from_paragraphs = inaugural.paras(os.path.dirname(__file__) + '/dataset/paragraphs.txt')
corpus_from_sentences = inaugural.sents(os.path.dirname(__file__) + '/dataset/sentences.txt')
corpus_from_words = inaugural.words(os.path.dirname(__file__) + '/dataset/words.txt')

l1 = len(corpus_from_paragraphs)
l2 = len(corpus_from_sentences)
l3 = len(corpus_from_words)
# l2 = 0
# l3 = 0
print('paragraphs: %s, sentences: %s, words: %s' % (l1, l2, l3))

# print(inaugural.readme())