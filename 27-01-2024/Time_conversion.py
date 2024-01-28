import math
import os
import random
import re
import sys


def timeConversion(s):
    hour, minute, second = map(int, s[:-2].split(':'))
    period = s[-2:]
    if period == 'PM' and hour != 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0

    result = '{:02d}:{:02d}:{:02d}'.format(hour, minute, second)

    return result

  
if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
