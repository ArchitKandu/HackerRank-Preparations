#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    n=int(s[0:2])
    s1=''
    if s[8]=='P':
        if n<12:
            n+=12
        elif n==12:
            n=12
        s1=str(n)
    elif s[8]=='A':
        if n<12:
            return s[0:8]
        elif n==12:
            s1='00'
    rstr=s1+s[2:8]
    return rstr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
