class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort
        return sorted(s) == sorted(t)