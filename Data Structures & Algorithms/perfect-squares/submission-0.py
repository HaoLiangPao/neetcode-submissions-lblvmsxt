class Solution:
    def numSquares(self, n: int) -> int:
        # Get the maximum square we need
        max_square = int(n ** 0.5)
        
        sqaures = [i * i for i in range(max_square + 1)]

        dp = [float('inf')] * (n+1)
        # Base Case
        dp[0] = 0

        # NP[i] = NP[i - SQUARE[j]] + 1 (for all j in sqaures)
        for i in range(1, n + 1):
            for square in sqaures:
                if square > i:
                    continue
                else:
                    dp[i] = min(dp[i], dp[i-square] + 1)
        
        return dp[n]