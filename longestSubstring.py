#!/usr/bin/python
'''
Given a string, find the length of the longest substring without repeating characters.
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring
'''

'''
Approach
    Maintain a dict of each char
    Loop through string
        If key does not exist, add key to current seq
        If key exists, check if the len of current seq is longer than longest seq
        if true: 
            len of current seq becomes longest seq
            Init dict again and add the current pointer as key to dict
    return len of longest subseq
'''
class Solution(object):
    def lengthOfLongestSubstring(self, string):
        """
        :type s: str
        :rtype: int
        """
        subseq = {}
        longest_len = 0
        for s in string:
            if s in subseq.keys():
                print(subseq.keys())
                if len(subseq) > longest_len:
                    longest_len = len(subseq)
                    subseq = {}
                    subseq[s] = 1
            else:
                print(subseq.keys())
                subseq[s] = 1
        print(subseq.keys())
        return longest_len

#string = "GEEKSFORGEEKS"
string = "ABDEFGABEF"
subsequence = Solution()
length = subsequence.lengthOfLongestSubstring(string)
print(length)