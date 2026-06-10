class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Subproblem: T[i][j] The longest common subsequence between the text1 till ith index and the text2 till jth index
        # Base Case: T[0][0] = 0, T[1][0] = 0, T[0][1] = 0
        T = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        # Recursion: T[i][j] = max(T[i-1][j])
        # 1) if text1[i] == text2[j]: T[i][j] = T[i-1][j-1] + 1
        # 2) if text1[i] != text2[j]:
        #   1) T[i][j] = T[i-1][j]
        #   2) T[i][j] = T[i][j-1]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    T[i][j] = T[i-1][j-1] + 1
                else:
                    T[i][j] = max(T[i-1][j], T[i][j-1])
        
        return T[-1][-1]