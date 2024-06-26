#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

#link to tHE PROBLEM: https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonalDifference(arr):
    left_diag=0
    right_diag=0
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            if i==j:
                left_diag+=arr[i][j]
            if (i+j==(len(arr)-1)):
                right_diag+=arr[i][j]
    return abs(left_diag-right_diag)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
