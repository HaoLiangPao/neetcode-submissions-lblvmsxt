class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s_mapping = {}
        char_t_mapping = {}
        for char in s:
            char_s_mapping[char] = 1 if char not in char_s_mapping else char_s_mapping[char] + 1
        for char in t:
            char_t_mapping[char] = 1 if char not in char_t_mapping else char_t_mapping[char] + 1
        return char_s_mapping == char_t_mapping