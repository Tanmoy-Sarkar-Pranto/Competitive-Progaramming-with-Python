nums = [16,4,10,14,7,9,3,2,8,1]

n = len(nums)

def left_child(i):
    return 2*i+1

def right_child(i):
    return (2*i)+2

def parent(i):
    return (i-1)//2

def max_heapify(i):
    left = left_child(i)
    right = right_child(i)
    largest = i
    if left<=n-1 and nums[left]>nums[largest]:
        largest = left
    
    if right<=n-1 and nums[right]>nums[largest]:
        largest = right
    
    if largest!=i:
        nums[i], nums[largest] = nums[largest], nums[i]
        max_heapify(largest)

for i in range((n//2)-1,-1,-1):
    max_heapify(i)

print(nums)