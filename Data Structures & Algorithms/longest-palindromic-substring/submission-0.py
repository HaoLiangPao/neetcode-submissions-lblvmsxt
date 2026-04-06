class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        # All char is a palindrom with length 1
        table = [[0 for _ in range(N)] for _ in range(N)]
        longest = 0
        l_index = 0
        r_index = 0

        for i in range(N-1, -1, -1):
            for j in range(i, N):
                if s[i] == s[j]:
                    # Base Case
                    if j == i:
                        table[i][j] = 1
                    elif j == i + 1:
                        table[i][j] = 2
                    # Recurrence
                    else:
                        if table[i+1][j-1] > 0:
                            table[i][j] = table[i+1][j-1] + 2
                    # As we will be returning the final result
                    if table[i][j] > longest:
                        longest = table[i][j]
                        l_index = i
                        r_index = j
        
        # print(table)
        # print(l_index, r_index)
        return s[l_index:r_index+1]