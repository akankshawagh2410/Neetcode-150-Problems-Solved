# Leetcode Problem 49: Group Anagrams
'''
Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order. An anagram is a string that contains the exact 
same characters as another string, but the order of the characters can be different.
'''
# Code Solution: 

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        return list(anagram_map.values())

# Link to the code explanation: https://medium.com/@akankshawagh/neetcode-150-solutions-explained-arrays-hashing-ed0c6184f387
