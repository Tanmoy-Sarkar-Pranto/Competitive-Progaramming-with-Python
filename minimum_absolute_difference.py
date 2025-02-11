import math

def minimumAbsoluteDifference(arr):
    min_diff = math.inf
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j:
                min_diff = min(min_diff, abs(arr[i]-arr[j]))
    
    return min_diff


print(minimumAbsoluteDifference([3,-7,0]))