"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

"""
Approach 1: Brute force
Time complexity O(n^2)
"""
def twosum_1(input, target):
    for i in range(0,len(input)):
        for j in range(1, len(input)-1):
            if input[i] + input[j] == target:
                return [i,j]

"""
Approach 2: Two pointer technique
Time complexity O(n)
- First sort in ascending order
- P1 will start from first element, P2 start from last element
- if sum smaller than target, we need a bigger number and since P2 points to the largest number in the array we can only shift P1 
- If sum bigger than target, then shift P2 left
"""
def twosum(input, target):
    input = sorted(input)
    p1 = 0
    p2 = len(input) - 1
    flag = True
    while(flag):
        if input[p1] + input[p2] == target:
            return [p1, p2]
        if input[p1] + input[p2] < target:
            p1 = p1 + 1
        if input[p1] + input[p2] > target:
            p2 = p2 - 1

print(twosum([2, 7, 11, 15], 9))
print(twosum([11,15,7,2,1], 9))
    