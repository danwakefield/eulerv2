#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text
file containing over five-thousand first names, begin by sorting it
into alphabetical order. Then working out the alphabetical value for
each name, multiply this value by its alphabetical position in the
list to obtain a name score. For example, when the list is sorted into
alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 ×
53 = 49714. What is the total of all the name scores in the file?

Answer: 871198282
"""
from __future__ import print_function
from utils import timer, word_score

with open('./data/022_names_scores.txt', 'r') as f:
    DATA = f.readlines()
    DATA = DATA[0].replace('"', '').split(',')
    DATA = sorted(DATA)


@timer
def main():
    total = 0

    for i, name in enumerate(DATA):
        total += (i+1) * word_score(name)

    return total


if __name__ == '__main__':
    print(main())
