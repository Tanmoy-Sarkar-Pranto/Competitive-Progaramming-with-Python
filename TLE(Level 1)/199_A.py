n = int(input())

if n==0:
    print(f"0 0 0")
elif n==1:
    print(f"0 0 1")
elif n==2:
    print(f"0 1 1")
else:
    fibonacci_series = []

    f0 = 0
    f1 = 1

    fibonacci_series.append(f0)
    fibonacci_series.append(f1)

    while fibonacci_series[-1]<n:
        new_f = f0 + f1
        fibonacci_series.append(new_f)
        f0, f1 = f1, new_f

    print(f"{fibonacci_series[-3]} {fibonacci_series[-3]} {fibonacci_series[-4]}")