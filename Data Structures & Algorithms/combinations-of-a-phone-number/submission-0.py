class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = [""]
        digit_map = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": "+"
        }

        def backtrack(cur, digit):
            tmp = cur
            for letter in digit_map[digit]:
                result.append(f"{tmp}{letter}")

        for digit in digits:
            total = len(result)
            count = 0
            while count < total:
                cur = result.pop(0)
                backtrack(cur, digit)
                # print(result)
                count += 1
        return [] if len(result) == 1 else result