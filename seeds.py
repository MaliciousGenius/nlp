#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import requests
import lxml.html

seeds_filename = "seeds.txt"
seeds_dirname = "./seeds"

try:
    os.mkdir(seeds_dirname)
except:
    print("Seeds directory alredy exist")

try:
    for line in open(seeds_filename, 'r+').readlines():
        response = requests.request('get', 'https://ru.wikipedia.org/wiki/' + line.strip('\n'))
        html = lxml.html.fromstring(response.text)
        text = html.text_content()
        with open(seeds_dirname + '/' + line.strip('\n') + '.html', 'w+') as out:
            out.write(text)
except:
    print("Seeds file not found")
