def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

nums = [1,3,8,2,9,2,5,6]
bubble_sort(nums)
print(nums)