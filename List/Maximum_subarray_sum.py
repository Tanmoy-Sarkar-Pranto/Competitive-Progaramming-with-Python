nums = [-1,4,2,-3,5,2,-5,2]
best = 0
# Brute Force n^3
def max_subarray_sum_brute_force(new_nums):
    for i in range(len(new_nums)):
        global best
        for j in range(i, len(new_nums)):
            total = 0
            for k in range(i, j+1):
                total += new_nums[k]
            best = max(best, total)


max_subarray_sum_brute_force(nums)
print(best)

# n^2
def max_subarray_sum_brute_force_better(new_nums):
    for i in range(len(new_nums)):
        global best
        total = 0
        for j in range(i, len(new_nums)):
            total += new_nums[j]
            best = max(best, total)

max_subarray_sum_brute_force_better(nums)
print(best)

def max_subarray_sum_kadane(new_nums):
    global best
    total = 0
    for num in new_nums:
        total = max(num, total+num)
        best = max(best, total)

max_subarray_sum_kadane(nums)
print(best)

