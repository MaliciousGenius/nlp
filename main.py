#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @package bot
# @brief Основной модуль приложения.

import sys
import urllib.request

inFile = sys.argv[1]
outFile = sys.argv[2]


def gethtml(url):
    try:
        response=requests.request('get',url,headers=header,timeout=30)
        response.raise_for_status()
        response.encoding=response.apparent_encoding
        html=response.content
    except:
        print("error")
    return html

with open(inFile, 'r+') as input, open(outFile,'w+') as out:
    for line in input:
        if len(line) > 1:
            html = gethtml("https://ru.wikipedia.org/wiki/" + line)
            out.write(str(html))

