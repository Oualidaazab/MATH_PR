def handshake(n):
    # Write your code here
    return (n*(n - 1)) / 2
# Number of tesr case  
t=int(input('Enter test case numbers  : ')) 
for t_ in range(t) : 
    n=int(input().strip()) 
# Number of handshake  : 
print(handshake(n)) 
