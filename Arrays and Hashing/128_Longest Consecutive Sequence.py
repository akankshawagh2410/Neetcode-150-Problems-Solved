# Leetcode Problem 128: Longest Consecutive Sequence
'''
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
The elements do not have to be consecutive in the original array. You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7

Constraints:
0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
'''
# Code Solution: 

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen = set(nums)
        best = 0

        for x in seen:
            if (x - 1) not in seen:
                length = 1
                curr = x
                while (curr + 1) in seen:
                    curr += 1
                    length += 1
                best = max(best, length)

        return best

# Link to the code explanation: https://medium.com/@akankshawagh/neetcode-150-solutions-explained-arrays-hashing-ed0c6184f387
