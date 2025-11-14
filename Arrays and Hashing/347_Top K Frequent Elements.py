# Leetcode Problem 347: Top K Frequent Elements
'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.
'''
# Code Solution: 
from collections import Counter
from heapq import nlargest
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        return [num for num, _ in nlargest(k, freq_map.items(), key=lambda x: x[1])]

# Link to the code explanation: https://medium.com/@akankshawagh/neetcode-150-solutions-explained-arrays-hashing-ed0c6184f387
