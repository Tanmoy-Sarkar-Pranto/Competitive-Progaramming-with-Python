import sys
sys.set_int_max_str_digits(1000000)

def fibonacciModified(t1, t2, n):
    if n==1:
        return t1
    if n==2:
        return t2
    for i in range(n-2):
        res = t1 + (t2*t2)
        t1, t2 = t2, res
    print(res)
    return res

print(fibonacciModified(1,1,20))