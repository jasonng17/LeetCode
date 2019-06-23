"""
Implement binary search
"""

def binarysearch(arr, target):
    low = 0
    high = len(arr)
    while low < high:
        mid = (high + low) // 2
        if arr[mid] > target:
            high = mid + 1
        elif arr[mid] < target:
            low = mid - 1
        else:
            return mid
    return -1

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10

# Function call 
result = binarysearch(arr, x) 
  
if result != -1: 
    print("Element is present at index {}".format(result))
else: 
    print ("Element is not present in array")