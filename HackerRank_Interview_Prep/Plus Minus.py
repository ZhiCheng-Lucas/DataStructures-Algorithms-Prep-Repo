#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    positive_count = 0
    negative_count = 0
    zero_count = 0
    total = len(arr)

    for i in arr:
        if i == 0:
            zero_count += 1
        elif i > 0:
            positive_count += 1
        else:
            negative_count += 1

    print(f"{positive_count/total:6f}")
    print(f"{negative_count/total:6f}")
    print(f"{zero_count/total:6f}")


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
