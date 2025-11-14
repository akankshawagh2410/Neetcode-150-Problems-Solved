# Leetcode Problem 271: Encode and Decode Strings
'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
Please implement encode and decode
'''
# Code Solution: 
from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded.append(s[j+1:j+1+length])
            i = j + 1 + length
        return decoded

# Link to the code explanation: https://medium.com/@akankshawagh/neetcode-150-solutions-explained-arrays-hashing-ed0c6184f387
