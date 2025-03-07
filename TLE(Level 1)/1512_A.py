from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))[:n]
    counter = Counter(nums)
    for k,v in counter.items():
        if v==1:
            print(nums.index(k)+1)
            break