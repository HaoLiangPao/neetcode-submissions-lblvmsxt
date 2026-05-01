class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)
        
        start, end = 0, 0
        count = [0] * 26

        while end < len(s):
            count[ord(s[end]) - ord('A')] += 1          # fix 1 & 2: use s[end], map char → index
            end += 1

            if (end - start) - max(count) > k:      # fix 3: invalid when replacements needed > k
                count[ord(s[start]) - ord('A')] -= 1    # fix 4: decrement before moving start
                start += 1

        return end - start
