# Leetcode Problem 217: Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Code Solution: 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
	seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Link to Explanation of code: https://medium.com/@akankshawagh/neetcode-150-solutions-explained-arrays-hashing-ed0c6184f387
