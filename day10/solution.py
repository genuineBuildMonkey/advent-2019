#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from shapely.geometry import Point, LineString


with open('input', 'r') as f:
    lines = f.read().splitlines()

    lines = [ 
    '.#..#',
    '.....',
    '#####',
    '....#',
    '...##']

    #lines = [
        #'......#.#.',
        #'#..#.#....',
        #'..#######.',
        #'.#.#.###..',
        #'.#..#.....',
        #'..#....#.#',
        #'#..#....#.',
        #'.##.#..###',
        #'##...#..#.',
        #'.#....####'
    #]

nodes = []

def part1():

    for r in range(len(lines)):
        row = lines[r]
        for c in range(len(lines)):
            char = row[c]

            if char == '#':
                p = Point(r, c) 
                nodes.append(p)

    ref = {}

    for node1 in nodes:
        #print(node1.x, node1.y)

        ref[(node1.x, node1.y)] = 0

        for node2 in nodes:
            if node1 == node2:
                continue

            l = LineString([node1, node2])

            valid = False

            #TODO restrict cross search forwards/backwards
            for node_cross in nodes:
                if node_cross == node1 or node_cross == node2:
                    continue

                if l.intersects(node_cross):
                    valid = False
                    break
                else:
                    valid = True

            if valid == True:
                ref[(node1.x, node1.y)] += 1

    ref_reverse = {v: k for k, v in ref.items()}

    greatest = max(ref.values())
    
    return greatest, ref_reverse[greatest]


def part2():
    pass



if __name__ == '__main__':
    p1 = part1()
    base = p1[1]
    print('part 1:', p1)
