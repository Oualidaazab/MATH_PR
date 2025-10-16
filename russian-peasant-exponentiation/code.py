#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. LONG_INTEGER k
#  4. INTEGER m
#

def solve(a, b, k, m):
    # Russian Peasant Exponentiation for complex numbers (a + bi)^k mod m
    real, imag = 1, 0
    base_real, base_imag = a % m, b % m

    while k > 0:
        if k % 2 == 1:
            # multiply (real + imag*i) * (base_real + base_imag*i)
            new_real = (real * base_real - imag * base_imag) % m
            new_imag = (real * base_imag + imag * base_real) % m
            real, imag = new_real, new_imag

        # square the base
        new_base_real = (base_real * base_real - base_imag * base_imag) % m
        new_base_imag = (2 * base_real * base_imag) % m
        base_real, base_imag = new_base_real, new_base_imag

        k //= 2

    return [real, imag]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])
        k = int(first_multiple_input[2])
        m = int(first_multiple_input[3])

        result = solve(a, b, k, m)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
#-------------------------------------------------------------| 
# i use thia formule 
#   (x1​+y1​i)×(x2​+y2​i)=(x1​x2​−y1​y2​)+(x1​y2​+x2​y1​)i
# 
#-------------------------------------------------------------