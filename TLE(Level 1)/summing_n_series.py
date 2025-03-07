t = int(input())

for _ in range(t):
    n = int(input())
    total = 0
    for i in range(n):
        total += (i+1)**2 - i**2

    print(total)