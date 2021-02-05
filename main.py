#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @package bot
# @brief Основной модуль приложения.

import sys
import urllib.request

inFile = sys.argv[1]
outFile = sys.argv[2]

def gethtml(url1):
    headers = {
       'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = urllib.request.Request(
    url = url1,
    headers = headers
    )
    html = urllib.request.urlopen(req).read()
    return html

with open(inFile, 'r+') as input, open(outFile,'w+') as out:
    for line in input:
        if len(line) > 1:
            html = gethtml("https://ru.wikipedia.org/wiki/" + line)
            out.write(str(html))


