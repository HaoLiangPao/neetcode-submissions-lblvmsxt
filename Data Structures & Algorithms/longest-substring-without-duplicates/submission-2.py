class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Edge Case
        if len(s) <= 1:
            return len(s)
        
        start, end = 0, 1
        tmp = set(s[start])
        result = 0

        while start < end and end < len(s):
            if s[end] in tmp:
                result = len(tmp) if len(tmp) > result else result
                # Find the first starting index that is not the same as the current duplicate char
                start += 1
                while start < end and s[start] == s[end]:
                    start += 1
                end = start + 1
                tmp = set(s[start])
            else:
                tmp.add(s[end])
                end += 1
        result = len(tmp) if len(tmp) > result else result
        return result