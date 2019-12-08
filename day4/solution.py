#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

puzzle_input = '124075-580769'


def part1():
    count = 0
    for n in range(124075, 580769):
        s = str(n)

        ispass = False
        foundDouble = False

        for i in range(len(s)):
            tl = s[i]
            try:
                tn = s[i + 1]
            except:
                continue

            if tn >= tl:
                if tn == tl:
                    foundDouble = True

            else:
                foundDouble = False
                ispass = False
                break

        if foundDouble == True:
            count += 1
            
                
    return count


def part2():
    count = 0
    for n in range(124075, 580769):
        s = str(n)

        ispass = False
        foundDouble = False

        for i in range(len(s)):
            tl = s[i]
            try:
                tn = s[i + 1]
            except:
                continue

            if tn >= tl:
                if tn == tl:

                    if re.search(r'%s{3}' % tn, s):
                        if not foundDouble:
                            foundDouble = False
                    else:
                        foundDouble = True

            else:
                foundDouble = False
                ispass = False
                break

        if foundDouble == True:
            count += 1
            
                
    return count


if __name__ == '__main__':
    print('1', part1())
    print('2', part2())
