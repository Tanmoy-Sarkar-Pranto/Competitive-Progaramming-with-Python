a, b = list(map(int, input().split()))

print("Multiples" if a%b==0 or b%a==0 else "No Multiples")