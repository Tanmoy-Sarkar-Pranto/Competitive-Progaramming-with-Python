# def sum_series(n, sum):
#     if n==0:
#         return 0
#     return n+sum_series(n-1, sum)

# sum = 0
# print(sum_series(10,sum=sum))


def sum_series(nums):
    if len(nums)<=0:
        return 0
    
    return nums[0] + sum_series(nums[1:])


print(sum_series([5,2,4,8, 10]))