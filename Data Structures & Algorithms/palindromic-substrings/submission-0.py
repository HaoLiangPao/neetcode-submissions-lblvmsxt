class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        table = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(N-1, -1, -1):
            for j in range(i, N):
                if s[i] == s[j]:
                    # Base Case:
                    # Each char is a palindrom
                    if i == j:
                        table[i][j] = 1
                    # Length 2 palindrom
                    elif j == i + 1:
                        table[i][j] = 1
                    else:
                        if table[i+1][j-1] > 0:
                            table[i][j] = 1
        
        # print(table)
        return sum([sum(row) for row in table])
