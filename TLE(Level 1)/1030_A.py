n = int(input())

peoples = list(map(int, input().split()))

print("HARD" if peoples.__contains__(1) else "EASY")