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
    count_zero=0.0
    count_pos=0.0
    count_neg=0.0
    n=len(arr)
    for ele in arr:
        if ele>0:
            count_pos+=1
        elif ele<0:
            count_neg+=1
        else:
            count_zero+=1
    print(round(count_pos/n, 6))
    print(round(count_neg/n, 6))
    print(round(count_zero/n, 6))
    
    
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
