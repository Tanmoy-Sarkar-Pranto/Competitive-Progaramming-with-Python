def iq_test(nums):
    even_conuter, last_even, last_odd = 0, 0, 0
    for i, num in enumerate(nums):
        if num%2==0:
            even_conuter+=1
            last_even=i+1
        else:
            even_conuter-=1
            last_odd=i+1
    
    return last_even if even_conuter<0 else last_odd

n = int(input())
nums = list(map(int, input().split()))[:n]
print(iq_test(nums))