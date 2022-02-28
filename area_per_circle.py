#!/usr/bin/env python3

# Created by Marc Coffi
# Created on February 2022

'''
 This is a program that calculates the area and the circumference
 of a circle with a radius of 15mm.
'''

import math


def main():
    print("If a circle has a radius of 15mm")
    print("The Area is {}mm^2".format(math.pi*(15**2)))
    print("The Circumference is {}mm".format(2*(math.pi*15)))


if __name__ == "__main__":
    main()
