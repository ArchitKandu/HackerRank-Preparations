#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    res=[]
    for i in grades:
        if i%5==0:
            res.append(i)
        else:
            if i>=38:
                t=int(i/5)
                r=int(((t+1)*5)-i)
                if r<3:
                    res.append(i+r)
                else:
                    res.append(i)
            else:
                res.append(i)    
    return res;   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
