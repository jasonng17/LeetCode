"""
Longest Substring with AT MOST K Distinct Characters (ID: 340)
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

Idea:
- keep track of a sliding window of the longest substring
    - if the distinct char <= K, expand window (high++)
    - else, shift window (low++)

Algorithm:
    maxlen = 0
    for high in range(0,len(arr)):
        distinct = "".join(set(arr[low:high]))
        while len(distinct) > k:
            low += 1
            distinct = "".join(set(arr[low:high]))
        if len(distinct) <= k:
            maxlen = max(maxlen, len(distinct))
    return maxlen
"""

"""
def longest_substring_with_k_distinct(arr, k):
  low, maxlen = 0, 0
  for high in range(0,len(arr)):
    distinct = "".join(set(arr[low:high]))
    while len(distinct) > k:
      low += 1
      distinct = "".join(set(arr[low:high]))
    if len(distinct) <= k:
      maxlen = max(maxlen, high-low)
  return maxlen
"""

# What if you cannot use set() function?
def longest_substring_with_k_distinct(arr, k):
  distinct = {}
  low, maxlen = 0, 0
  for high in range(0,len(arr)):
    if arr[high] not in distinct.keys():
      distinct[arr[high]] = 1
    else:
      distinct[arr[high]] += 1
    while len(distinct) > k:
      if distinct[arr[low]] == 1:
        del distinct[arr[low]]
      else:
        distinct[arr[low]] -= 1
      low += 1
    maxlen = max(maxlen, high-low+1)
  return maxlen


def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
