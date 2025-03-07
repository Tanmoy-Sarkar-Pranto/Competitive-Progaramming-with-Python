t = int(input())

for _ in range(t):
    skills = list(map(int, input().split()))
    print("YES" if sorted([max(skills[0],skills[1]),max(skills[2],skills[3])], reverse=True) == sorted(skills, reverse=True)[:2] else "NO")

