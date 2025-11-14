# Leetcode Problem 1: Two Sum
'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j. 
You may assume that every input has exactly one pair of indices i and j that satisfy the condition. 
Return the answer with the smaller index first.
'''
# Code Solution: 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

# Link to the code explanation: [Link to the Blog](https://medium.com/@akankshawagh/neetcode-150-solutions-explained-arrays-hashing-ed0c6184f387)
