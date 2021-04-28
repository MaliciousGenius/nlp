#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def  create_stat_file():

    if os.path.exists("dataset/stats.txt"):
        os.remove("dataset/stats.txt")

    for txt_file in os.scandir("dataset"):
        if txt_file.is_file() and txt_file.path.split('.')[-1].lower() == "txt":
            counter = 0
            for line in open(txt_file, "r+").readlines():
                counter += 1
            with open("dataset/stats.txt", "a") as out:
                out.write("file: " + txt_file.path.split('.')[-2].lower() + " count: " + str(counter) + "\n")

def main():
    create_stat_file()

if __name__ == '__main__':
    main()
