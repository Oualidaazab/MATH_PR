import math
import os

def solve(n):
    MOD = 1000007
    
    # If n >= MOD, then n! will contain MOD as a factor
    # So (n!)^2 mod MOD = 0
    if n >= MOD:
        return 0
    
    # Compute n! mod MOD
    factorial = 1
    for i in range(1, n + 1):
        factorial = (factorial * i) % MOD
    
    # Return (factorial)^2 mod MOD
    return (factorial * factorial) % MOD

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = solve(n)
    fptr.write(str(result) + '\n')

    fptr.close()
