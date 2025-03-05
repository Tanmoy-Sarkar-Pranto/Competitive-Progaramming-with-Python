n = input()

n = n.split(".")

if int(n[1])!=0:
    print(f"float {n[0]} 0.{n[1]}")
else:
    print(f"int {n[0]}")