#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    # Write your code here
    """
    count how many times the most and least changes
    """

    max_score = min_score = scores[0]
    changes = [0, 0]

    for i in range(1, len(scores)):
        if scores[i] > max_score:
            changes[0] += 1
            max_score = scores[i]
        if scores[i] < min_score:
            changes[1] += 1
            min_score = scores[i]

    return changes


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
