#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

masses = open('input.txt', 'r').readlines()


def part1():
    return sum([((int(i.strip()) / 3) - 2) for i in masses])


def part2():
    total = 0

    for m in masses:
        m = int(m.strip())

        requires = math.floor((m / 3) - 2)
        total += requires

        while requires > 0:
            requires = math.floor((requires / 3) - 2)

            if requires > 0:
                total += requires


    return total


print(part1())
print(part2())
