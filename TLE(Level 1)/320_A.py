n = input()

window = []
for i in range(len(n)-1,-1,-1):
    if len(window)<=0:
        if n[i] in ["1","14","144"]:
            continue

    window.append(n[i])
    num = "".join(reversed(window))
    if num in ["1", "14", "144"]:
        window.clear()
        continue

if len(window)>0:
    print("NO")
else:
    print("YES")