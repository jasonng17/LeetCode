"""
Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Idea:
- The brute force approach would be to merge into a single array
    - Median is the middle number for an array of odd length
    - Median is the avg of the middle 2 numbers for an array of even length
- Whenever you see sorted array, it is a hint that this is a binary search problem
- You know that the medium for two arrays must be somewhere in between the medium of each of the 2 arrays.
- CONDITION: We want to partition the 2 arrays such that the number of elements in each half is the same AND the elements in the left half must be smaller or equal to every element in the right half
- If we take x elements from the first array to our left part, it means that we need to take (len(a) + len(b) + 1) / 2 — x elements from the second array.

Reference:
https://www.youtube.com/watch?v=LPFhl65R7ww&t=1252s
"""

import sys
import time
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    # Swap position if nums1 is greater length than nums2
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)
    
    high = len(nums1)
    low = 0
    x = len(nums1)
    y = len(nums2)

    while low <= high:
        partitionX = (high+low)//2
        partitionY = (x+y+1)//2 - partitionX
        print("Low is {} and High is {}".format(low, high))
        print("Partition X is {} and Partition Y is {}".format(partitionX, partitionY))
        maxleftX = -sys.maxsize if partitionX == 0 else nums1[partitionX - 1]
        maxleftY = -sys.maxsize if partitionY == 0 else nums2[partitionY - 1]
        minrightX = sys.maxsize if partitionX == x else nums1[partitionX]
        minrightY = sys.maxsize if partitionY == y else nums2[partitionY]
        if maxleftX <= minrightY and maxleftY <= minrightX:
            if (x+y) % 2 == 0:
                return (max(maxleftX, maxleftY) + min(minrightX, minrightY)) / 2
            else:
                return max(maxleftX, maxleftY)
        elif maxleftY > minrightX:
            low = partitionX + 1
        elif maxleftX > minrightY:
            high = partitionX - 1
        time.sleep(1)

nums2 = [23,26,31,35]
nums1 = [3,5,7,9,11,16]
result = findMedianSortedArrays(nums1, nums2)
if result != -1: 
    print("Median {}".format(result))
else: 
    print ("Median cannot be found")
"""
nums1 = [1,3,8,9,15]
nums2 = [7,11,18,19,21,25]
result = findMedianSortedArrays(nums1, nums2)
if result != -1: 
    print("Median is {}".format(result))
else: 
    print ("Median cannot be found")
"""
