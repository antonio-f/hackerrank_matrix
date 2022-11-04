#!/bin/python3
# HackerRank's Matrix problem

import math
import os
import random
import re
import sys

#
# Complete the 'minTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY roads
#  2. INTEGER_ARRAY machines
#

class Rec:
    def __init__(self, nodes, machine):
        self.nodes = set([nodes])
        self.machine = machine

def minTime(roads, machines):
    res = 0
    m = set(machines)
    d = dict()
    r = sorted(roads, key=lambda x: x[2], reverse=True)
    for a, b, w in r:
        d[a] = d.get(a, Rec(a, a in m))
        d[b] = d.get(b, Rec(b, b in m))
        s1, s2 = d[a], d[b]
        if s1 == s2: continue
        if s1.machine and s2.machine: res += w; continue
        s1.nodes.update(s2.nodes)
        s1.machine = s1.machine or s2.machine
        for c in s2.nodes: d[c] = s1
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    machines = []

    for _ in range(k):
        machines_item = int(input().strip())
        machines.append(machines_item)

    result = minTime(roads, machines)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
