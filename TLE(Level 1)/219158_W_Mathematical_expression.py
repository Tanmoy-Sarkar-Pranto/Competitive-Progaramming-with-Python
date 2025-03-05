a, s, b, q, c = list(map(str, input().split()))
a, b, c = int(a), int(b), int(c)

if s=="+":
    if a + b == c:
        print("Yes")
    else:
        print(a + b)
elif s=="-":
    if a - b == c:
        print("Yes")
    else:
        print(a - b)
elif s=="*":
    if a * b == c:
        print("Yes")
    else:
        print(a * b)