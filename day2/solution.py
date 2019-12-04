#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import itertools



#def main():
def part1():
    with open('input.txt', 'r') as f:
        #masses = f.readlines()
        masses = f.read().splitlines()

        nums = [int(i) for i in masses[0].split(',')]

    c = 0
    #l = []
    ll = len(nums)

    nums[1] = 12
    nums[2] = 2

    while c < ll - 1:

        curnum = nums[c]

        if curnum == 1:

            s = nums[nums[c + 1]] + nums[nums[c + 2]] 

            nums[nums[c + 3]] = s

            c += 4

            continue

        elif curnum == 2:
            s = nums[nums[c + 1]] * nums[nums[c + 2]] 

            print(s)

            nums[nums[c + 3]] = s

            c += 4

            print('y', nums)
            continue


        elif curnum == 99:
            c += 1
            continue


    return(nums[0])

def getdata():

    with open('input.txt', 'r') as f:
        masses = f.read().splitlines()

        nums = [int(i) for i in masses[0].split(',')]

    return nums

def part2():

    for noun in range(0, 100):

        for verb in range(0, 100):
            nums = getdata() 
            ll = len(nums)

            nums[1] = noun
            nums[2] = verb
            c = 0

            while c < ll:

                curnum = nums[c]

                if curnum == 1:

                    s = nums[nums[c + 1]] + nums[nums[c + 2]] 

                    nums[nums[c + 3]] = s

                    c += 4

                    if nums[0] == 19690720:
                       return(100 * noun + verb)

                    continue

                elif curnum == 2:
                    s = nums[nums[c + 1]] * nums[nums[c + 2]] 

                    #print(s)

                    nums[nums[c + 3]] = s

                    c += 4

                    if nums[0] == 19690720:
                        print('YY', noun, verb)
                    #print('y', nums)
                    continue


                elif curnum == 99:
                    c += 1
                    continue

            

def main():
    print('1', part1())
    print('2', part2())

if __name__ == '__main__':
    main()
