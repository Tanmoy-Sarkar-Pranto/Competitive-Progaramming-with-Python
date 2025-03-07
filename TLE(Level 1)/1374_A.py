t = int(input())

for _ in range(t):
    x, y, n = list(map(int, input().split()))
    k = (n // x) * x + y
    if k > n:
        k -= x
    print(k)
