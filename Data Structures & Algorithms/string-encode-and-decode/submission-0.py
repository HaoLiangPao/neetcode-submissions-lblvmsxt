class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        delimeter = "#"

        for string in strs:
            size = len(string)
            result += str(size) + delimeter + string
        
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        delimeter = "#"

        buff = ""
        i = 0
        while i < len(s):
            # Find the first <size>#<word> pair
            size_str = buff
            if s[i] == delimeter:
                size = int(size_str)
                word_start = i + 1 # skip delimeter '#'
                word_end = word_start + size
                # print(f"size is {size}, word_start is {word_start}, word_end is {word_end}")
                word = s[word_start:word_end]
                result.append(word)
                i = word_end # skip the word, look for the next pair
                buff = ""
            else:
                buff += s[i]
                i += 1
        return result