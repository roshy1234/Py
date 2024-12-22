#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    d = {}
    for i in s:
        d[i] = d.get(i,0)+1
    print(d)