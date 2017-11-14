#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Anna Klezovich
# 15.11.2017


import itertools
import csv


def func(fi_patterns, n):
    with open('all_combs.txt', 'a', encoding='utf-8') as file:
        for p in itertools.product(fi_patterns, repeat=n):
            file.write(str(p) + '\n')


def compare(file, f):
    with open(f, 'r', encoding='utf-8') as f1:
        d = csv.DictReader(f1, delimiter=';')
        table = []
        for line in d:
            table.append(line)
    with open(file, 'r', encoding='utf-8') as file1:
        s = file1.readlines()

    form_image = []
    for line in table:
        form_image.append(line['form-image assocaition pattern'])
    for el in s:
        el = el.strip('\n\r')
        if el not in form_image:
            print(el)


if __name__ == '__main__':
    #patterns = ['object', 'handling', 'contour', 'tracing', '-', '&', '+', '?']
    #func(patterns, 3)
    #func(patterns, 5)
    #func(patterns, 7)
    compare('combinations.txt', 'table.csv')
