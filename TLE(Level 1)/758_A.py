n = int(input())

buries = list(map(int, input().split()))

max_burie = max(buries)

total = 0

for i in buries:
    total += max_burie-i

print(total)
