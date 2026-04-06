class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two Pointer
        start = 0
        end = len(s) - 1

        while start + end < len(s) and start < end:
            print(f"start is {start}")
            print(f"end is {end}")

            while not (s[start].isalnum()) and start < len(s) - 1:
                start += 1
            while not (s[end].isalnum()) and end > 0:
                end -= 1 
            
            if start == len(s) - 1 and end == 0:
                return True

            if s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
        return True