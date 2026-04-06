class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_table = [[0 for _ in range(n)] for _ in range(m)]

        # Base Case:
        for i in range(m):
            for j in range(n):
                dp_table[i][0] = 1
                dp_table[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if i-1 >= 0 and i-1 <= m:
                    dp_table[i][j] += dp_table[i-1][j]
                if j-1 >= 0 and j-1 <= n:
                    dp_table[i][j] += dp_table[i][j-1]

        return dp_table[-1][-1]
