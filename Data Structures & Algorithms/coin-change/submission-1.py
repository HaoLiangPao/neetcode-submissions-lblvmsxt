class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        INF = 10001
        
        # table[coin_idx + 1][amount + 1] 
        # Adding a row for "0 coins available"
        table = [[INF for _ in range(amount+1)] for _ in range(N + 1)]
        
        # Base Case: Amount 0 always takes 0 coins
        for i in range(N + 1):
            table[i][0] = 0

        # Start from the first actual coin (index 1 in table, index 0 in coins)
        for i in range(1, N + 1):
            current_coin = coins[i-1]
            for j in range(1, amount + 1):
                # 1. Not include: Look at the row above
                not_include = table[i-1][j]

                # 2. Include: Look at the current row (leftwards)
                if j >= current_coin:
                    include = table[i][j - current_coin] + 1
                else:
                    include = INF
                
                table[i][j] = min(not_include, include)
        
        result = table[N][amount]
        return result if result < INF else -1