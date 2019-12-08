#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

width = 25
height = 6


with open('input.txt', 'r') as f:
    lines = f.read().splitlines()[0]

def part1():
    min_zero = 999999
    out = None

    for layer in list(map(''.join, zip(*[iter(lines)]*(width * height)))):
        zero_count = len(re.findall('0', layer))
        if zero_count < min_zero:
            min_zero = zero_count

            out = len(re.findall('1', layer)) * len(re.findall('2', layer))

    return out


def part2():
    current = []

    layers = list(map(''.join, zip(*[iter(lines)]*(width * height))))
    layers.reverse()

    for layer in layers:
        for i in range(len(layer)):
            value = layer[i]

            try:
                prev_value = current[i]
            except:
                current.append(layer[i])
                continue

            value = layer[i]

            if value in ['0', '1']:
                current[i] = value

            if value == '2':
                if prev_value == '0' or prev_value == '1':
                    current[i] = prev_value
                else:
                    current[i] = value

    current = ''.join(current)

    for i in range(height):
            print(current[(width * i): width * (i+1)] \
                    .replace('0', ' ').replace('1', '*'))



if __name__ == '__main__':
    print('1', part1())
    print('2', part2())
