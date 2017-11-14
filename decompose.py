#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Anna Klezovich
# 14.11.2017


import csv
import re


def read(f):
    with open(f, 'r', encoding='utf-8') as file:
        d = csv.DictReader(file, delimiter=';')
        table = []
        for line in d:
            table.append(line)
    return table


def parse(data):
    fieldnames = ['word', 'semantic field', 'image-concept association',
                  'form-image assocaition pattern', 'non iconic',
                  'languages', 'urls', 'Localization ', 'Personification',
                  'Action', 'Parts/wholes', 'Two hand signs', 'Compounds']

    with open('refactored_table.csv', 'w', newline='', encoding='utf-8') as out:
        out_csv = csv.writer(out, delimiter=';')

        out_csv.writerow(fieldnames)
        for line in data:
            m = re.findall('&', line['Action'])
            if m != []:
                match_a = re.search('(.+)?&(.+)?', line['Action'])
                match_l = re.search('(.+)?&(.+)?', line['Localization '])
                match_pattern = re.search('(.*)?&(.*)?', line['form-image assocaition pattern'])
                if match_pattern is None:
                    pass
                else:
                    mat_1 = match_pattern.group(1)
                    mat_2 = match_pattern.group(2)
                match_part = re.search('(.+)?&(.+)?', line['Parts/wholes'])
                match_p = re.search('(.+)?&(.+)?', line['Personification'])
                match_non = re.search('(.*)&(.*)', line['non iconic'])

                if match_non:
                    left_non = match_non.group(1)
                    right_non = match_non.group(2)
                else:
                    left_non = '0'
                    right_non = '0'

                out_csv.writerows([[line['word'], line['semantic field'], line['image-concept association'],
                                    mat_1, left_non, line['languages'],
                                    line['urls'], match_l.group(1), match_p.group(1),
                                    match_a.group(1), match_part.group(1), line['Two hand signs'], 'first'],
                                   [line['word'], line['semantic field'], line['image-concept association'],
                                    mat_2, right_non, line['languages'],
                                    line['urls'], match_l.group(2), match_p.group(2),
                                    match_a.group(2), match_part.group(2), line['Two hand signs'], 'second']])

            else:
                out_csv.writerow([line['word'], line['semantic field'], line['image-concept association'],
                                  line['form-image assocaition pattern'], line['non iconic'], line['languages'],
                                  line['urls'], line['Localization '], line['Personification'],
                                  line['Action'], line['Parts/wholes'], line['Two hand signs'], line['Compounds']])


def parse_plus(data):
    fieldnames = ['word', 'semantic field', 'image-concept association',
                  'form-image assocaition pattern', 'non iconic',
                  'languages', 'urls', 'Localization ', 'Personification',
                  'Action', 'Parts/wholes', 'Two hand signs', 'Compounds']

    with open('refactored_table.csv', 'w', newline='', encoding='utf-8') as out:
        out_csv = csv.writer(out, delimiter=';')

        out_csv.writerow(fieldnames)
        for line in data:
            m2 = re.findall('\+', line['Action'])
            if m2 != []:
                match_a2 = re.search('(.+)?\+(.+)?', line['Action'])
                match_l2 = re.search('(.+)?\+(.+)?', line['Localization '])
                match_pattern2 = re.search('(.*)?\+(.*)?', line['form-image assocaition pattern'])
                if match_pattern2 is None:
                    pass
                else:
                    mat_12 = match_pattern2.group(1)
                    mat_22 = match_pattern2.group(2)

                match_part2 = re.search('(.+)?\+(.+)?', line['Parts/wholes'])
                match_p2 = re.search('(.+)?\+(.+)?', line['Personification'])

                out_csv.writerows([[line['word'], line['semantic field'], line['image-concept association'],
                                    mat_12, line['non iconic'], line['languages'],
                                    line['urls'], match_l2.group(1), match_p2.group(1),
                                    match_a2.group(1), match_part2.group(1), 'active', line['Compounds']],
                                   [line['word'], line['semantic field'], line['image-concept association'],
                                    mat_22, line['non iconic'], line['languages'],
                                    line['urls'], match_l2.group(2), match_p2.group(2),
                                    match_a2.group(2), match_part2.group(2), 'secondary', line['Compounds']]])
            else:
                out_csv.writerow([line['word'], line['semantic field'], line['image-concept association'],
                                  line['form-image assocaition pattern'], line['non iconic'], line['languages'],
                                  line['urls'], line['Localization '], line['Personification'],
                                  line['Action'], line['Parts/wholes'], line['Two hand signs'], line['Compounds']])


if __name__ == '__main__':
    data_1 = read('table.csv')
    parse(data_1)
    data_3 = read('refactored_table.csv')
    parse_plus(data_3)
    i = 0
    for i in range(0, 2):
        data_2 = read('refactored_table.csv')
        parse(data_2)
        data_4 = read('refactored_table.csv')
        parse_plus(data_4)
        i += 1
