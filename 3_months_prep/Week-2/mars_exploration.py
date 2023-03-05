#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    res=0
    for i in range(0,len(s),3):
        count=0
        t=s[i:i+3]
        if(t[0]!='S'):
            count+=1
        if(t[1]!='O'):
            count+=1
        if(t[2]!='S'):
            count+=1
        res+=count
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
