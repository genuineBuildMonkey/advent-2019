#!/usr/bin/env python
# -*- coding: utf-8 -*-

weights = open('input.txt', 'r').readlines()

solution = sum([((int(i.strip()) / 3) - 2) for i in weights]) 

print(solution)
