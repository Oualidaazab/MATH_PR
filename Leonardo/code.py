

#!/bin/python3

def primeCount(n):
    # List of prime numbers (enough for all test ranges)
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
              53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    product = 1
    count = 0
    for p in primes:
        product *= p
        if product > n:
            break
        count += 1
    return count


if __name__ == '__main__':
    q = int(input().strip())  # number of queries
    for _ in range(q):
        n = int(input().strip())
        print(primeCount(n))
