#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from gensim import corpora

lines = []

# Записываем все предложения в список
for line in open("sentences.txt", "r"):
    lines.append(line)

# Разбиваем тредложения на токены
tokens = [[token for token in line.split()] for line in lines]

# Создаем словарь токенов
dictionary = corpora.Dictionary(tokens)

# Сохраняем Словарь и Корпус
dictionary.save("tokens.dict")
dictionary.save_as_text("tokens.txt")

# import pandas
# from gensim import corpora

# df = pandas.read_csv('dataset/simple_definition.csv')
# simple_definitions = df['TEXT']
# words=[]

# for simple_definition in simple_definitions:
#     words.append(simple_definition.split(' '))

# dictionary = corpora.Dictionary(words)
# dictionary.save_as_text('./dict.txt')

# print(len(dictionary))

# Получаем информацию о словаре
# print(dictionary)