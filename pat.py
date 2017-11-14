#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Anna Klezovich
# 14.11.2017


import csv
import operator


def read(f):
    with open(f, 'r', encoding='utf-8') as file:
        d = csv.DictReader(file, delimiter=';')
        table = []
        for line in d:
            table.append(line)
    return table


def freq(data):
    form_image = {}
    for line in data:
        t = line['form-image assocaition pattern']
        if t not in form_image:
            form_image[t] = 1
        else:
            form_image[t] += 1
    with open('form_image_pattern.csv', 'w', newline='', encoding='utf-8') as out:
        out_csv = csv.writer(out, delimiter=';')

        out_csv.writerow(['patterns', 'frequency'])
        for row in sorted(form_image.items(), key=operator.itemgetter(1)):
            out_csv.writerow(row)


if __name__ == '__main__':
    data_1 = read('table.csv')
    freq(data_1)
