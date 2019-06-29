"""
Given an array, find the average of all subarrays of size ‘K’ in it.
Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]

Time complexity:
Brute force: O(MxN)
Sliding window: O(N)

Main idea:
- There are overlapping parts of the subarray that we do not need to sum up every time. Instead just remove the last element and add the next the the sum

Algorithm:
result = []
winStart, winSum = 0, 0.0
for winEnd until len(array):
    add to winSum
    if winEnd reaches window size:
        addavg to result
        remove winEnd from winSum
        increment winStart by 1
return result

https://www.educative.io/collection/page/5668639101419520/5671464854355968/6658855733821440
"""

def find_averages_of_subarrays(K, arr):
  result = []
  winStart, winSum = 0, 0.0
  for winEnd in range(0, len(arr)):
      winSum += arr[winEnd]
      if winEnd >= K-1:
          result.append(winSum/K)
          winSum -= arr[winStart]
          winStart += 1
  return result


def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()