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
- 
"""