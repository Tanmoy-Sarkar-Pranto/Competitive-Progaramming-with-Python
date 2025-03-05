t = int(input())

for _ in range(t):
    l, r = list(map(int, input().split()))
    if l>r:
        l, r = r, l
    sum_till_l = l*(l-1)//2
    sum_till_r = r*(r+1)//2
    print(sum_till_r - sum_till_l)