#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    # Time complexity. Sorting. nlogn
    # Space complexity. O(1).
    arr.sort()

    min_sum = sum(arr[:-1])
    max_sum = sum(arr[1:])

    print(f"{min_sum} {max_sum}")


if __name__ == "__main__":

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
