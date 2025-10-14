#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. LONG_INTEGER a
#  2. LONG_INTEGER b
#  3. LONG_INTEGER x
#  4. LONG_INTEGER y
#
def solve(a, b, x, y):
    # The key insight: we can reach (x, y) from (a, b) if and only if
    # gcd(a, b) divides both (x - a) and (y - b)
    # However, we also need to check if (x, y) can be represented as
    # a linear combination of moves from (a, b)
    
    # This is equivalent to checking if (x, y) and (a, b) are in the same
    # equivalence class under the moves, which relates to their GCD
    
    # Simple approach: simulate the reverse process
    # Work backwards from (x, y) to see if we can reach (a, b)
    
    def can_reach(a, b, x, y):
        # If we've reached the target
        if a == x and b == y:
            return True
        
        # If x or y is too small, we can't reach target
        if x < a or y < b:
            return False
        
        # Try moving backwards: reverse the operations
        # If we got to (x, y) via (x+y, y), then we came from (x, y)
        # If we got to (x, y) via (x, x+y), then we came from (x, y)
        # If we got to (x, y) via (x-y, y), then we came from (x, y)
        # If we got to (x, y) via (x, y-x), then we came from (x, y)
        
        while x > a or y > b:
            if x > y:
                # We likely came from (x - y, y) or similar
                x = x - y
            elif y > x:
                # We likely came from (x, y - x) or similar
                y = y - x
            else:
                # x == y
                break
        
        return a == x and b == y
    
    if can_reach(a, b, x, y):
        return "YES"
    else:
        return "NO"
     
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])
        x = int(first_multiple_input[2])
        y = int(first_multiple_input[3])
        result = solve(a, b, x, y)
        fptr.write(result + '\n')
    fptr.close()