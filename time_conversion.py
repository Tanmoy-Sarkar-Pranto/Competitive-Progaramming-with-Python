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
    # Write your code here
    times = s.split(":")
    print(times)
    new_time = ["00","00","00"]
    if times[2][2:] == "AM":
        if int(times[0])<12:
            new_time[0] = times[0]
        new_time[1] = times[1]
        new_time[2] = times[2][:2]
    else:
        if int(times[0])==12:
            new_time[0] = times[0]
        else:
            new_time[0] = str(int(times[0]) + 12)
        new_time[1] = times[1]
        new_time[2] = times[2][:2]

    return ":".join(new_time)
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()