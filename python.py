# import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n % 2 == 1:   # Check if n is add
    print('Weird')
elif n % 2 == 0 and 2 >= n >= 5: # Check n is even and inclusive range(>=) [2,5]
    print('Not Weird')
