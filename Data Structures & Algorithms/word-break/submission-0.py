class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        table = [False for _ in range(N+1)]

        wordDict = set(wordDict)

        # Base Case
        table[0] = True

        for i in range(1, N+1):
            for j in range(i): # 0<=j<i
                wordCheck = s[j:i] in wordDict
                if i == N:
                    print(f"wordCheck is (j,i): ({j}, {i}), {s[j:i]}, result: {wordCheck}")
                # Check if the left and right section of a pivot are both valid words (or word combinations)
                table[i] = table[i] or (table[j] and (wordCheck))

        # print(table)
        return table[-1]
