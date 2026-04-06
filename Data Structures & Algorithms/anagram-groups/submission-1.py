class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            count_map = [0] * 26
            for char in string:
                count_map[ord(char) - ord('a')] += 1
            if tuple(count_map) in anagrams:
                anagrams[tuple(count_map)].append(string)
            else:
                anagrams[tuple(count_map)] = [string]
        return list(anagrams.values())

    