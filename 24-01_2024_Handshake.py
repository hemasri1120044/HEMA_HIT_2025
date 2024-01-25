#At the annual meeting of Board of Directors of Acme Inc. If everyone attending shakes hands exactly one time with every other attendee, how many handshakes are there?
#Example.n=3
#There are 3 attendees,p1 ,p2 and p3. p1shakes hands with p2and p3 , and p2 shakes hands withp3. Now they have all shaken hands after  handshakes.


#Function Description
#Complete the handshakes function in the editor below.handshakes has the following parameter:
#int n: the number of attendees
#Returns
#int: the number of handshakes
#Input Format 
#The first line contains the number of test cases . 
#Each of the following  lines contains an integer, .
#Constraints
#Sample Input
#2
#1
#2
#Sample Output
#0
#1

import math
import os
import random
import re
import sys

def handshake(n):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()
