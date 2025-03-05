t = int(input())

for _ in range(t):
    evens,odds = 0, 0
    a = int(input())
    n = list(map(int, input().split()))
    if len(n)%2!=0:
        print(-1)
    else:
        for i in n:
            if i%2==0:
                evens += 1
            else:
                odds += 1
        print((abs(evens-odds))//2)