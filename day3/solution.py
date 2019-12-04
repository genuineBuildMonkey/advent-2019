#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shapely.geometry import LineString

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

    wire1_data = lines[0].split(',')
    wire2_data = lines[1].split(',')


def _build_line_string(points):
    nodes = [(0, 0)]
    pos = {'x': 0, 'y': 0}

    for point in points:

        d = point[0]
        l = int(point[1:])

        source_x = pos['x']
        source_y = pos['y']

        if d == 'U':
            pos['y'] += l
            nodes.append([source_x, pos['y']])

        elif d == 'D':
            pos['y'] -= l
            nodes.append([source_x, pos['y']])

        elif d == 'R':
            pos['x'] += l
            nodes.append([pos['x'], source_y])

        elif d == 'L':
            pos['x'] -= l
            nodes.append([pos['x'], source_y])

    return LineString(nodes)


def part1():
    line_1 = _build_line_string(wire1_data) 
    line_2 = _build_line_string(wire2_data) 

    crosses = line_1.intersection(line_2)

    distances = [abs(i.x) + abs(i.y) for i in crosses]

    return sorted(distances)[1]


def part2():
    line_1 = _build_line_string(wire1_data) 
    line_2 = _build_line_string(wire2_data) 

    crosses = line_1.intersection(line_2)

    distances = []

    for c in crosses:
        if c.x == 0 and c.y == 0:
            continue

        distances.append(line_1.project(c) + line_2.project(c))

    return sorted(distances)[0]


if __name__ == '__main__':
    print('1', part1())
    print('2', part2())
