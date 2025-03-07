import math

n, m = list(map(int, input().split()))

# a**2 + b = n, a + b**2 = m
# a<=sqrt(n), b<=sqrt(m)

count = 0
for a in range(int(math.sqrt(n))+1):
    for b in range(int(math.sqrt(m))+1):
        if a**2 + b == n and a + b**2 == m:
            count += 1

print(count)