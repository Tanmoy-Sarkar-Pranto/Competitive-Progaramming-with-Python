def total_degree(p: int, a: int, b: int, c: int)->int:
    total = 0
    total += 720 # First 2 clockwise full rotation, after this position back to p
    total += abs(p-a)*9 if p<=a else 360-((p-a)*9) # position to a
    total += 360 # 1 counter-clockwise rotation
    total += abs(a-b)*9 if a>=b else 360-((a-b)*9)
    total += abs(b-c)*9 if b<=c else 360-((b-c)*9)
    return total

while True:
    p, a, b, c = list(map(int, input().split()))
    if p==0 and a==0 and b==0 and c==0:
        break
    print(total_degree(p, a, b, c))