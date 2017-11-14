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
    all_patterns = {}
    for line in data:
        t = ' '.join([line['form-image assocaition pattern'], line['non iconic'], line['Localization '],
                      line['Personification'], line['Action'], line['Parts/wholes']])
        if t not in all_patterns:
            all_patterns[t] = 1
        else:
            all_patterns[t] += 1

    with open('freq_r.csv', 'w', newline='', encoding='utf-8') as out:
        out_csv = csv.writer(out, delimiter=';')

        out_csv.writerow(['patterns', 'frequency'])
        for row in sorted(all_patterns.items(), key=operator.itemgetter(1)):
            out_csv.writerow(row)


if __name__ == '__main__':
    data_1 = read('refactored_table.csv')
    freq(data_1)
