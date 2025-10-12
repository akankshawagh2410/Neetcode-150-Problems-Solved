#Leetcode Problem 242: Valid Anagram
'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false. 
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
'''
# My Code Solution: 17ms

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)

# Optimized Code Solution: 2ms

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Link to Explanation of code: 
