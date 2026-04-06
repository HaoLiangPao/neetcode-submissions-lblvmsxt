class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            count_map = [0] * 26
            for char in string:
                count_map[ord(char) - ord('a')] += 1
            anagrams[tuple(count_map)].append(string)
        return list(anagrams.values())

    