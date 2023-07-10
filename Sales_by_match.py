#There is a large pile of socks that must be paired by color.
# Given an array of integers representing the color of each sock,
# determine how many pairs of socks with matching colors there are.

# !/bin/python3

import math
import os
import random
import re
import sys
#
from collections import Counter


def sockMerchant(n, ar):
    # Write your code here
    sum = 0
    for val in Counter(ar).values():
        sum += val // 2
    return sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
