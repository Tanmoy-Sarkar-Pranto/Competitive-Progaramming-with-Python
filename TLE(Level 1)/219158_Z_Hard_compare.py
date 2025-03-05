import math

a, b, c, d = list(map(int, input().split()))

print("YES" if b*math.log(a)>d*math.log(c) else "NO")