class Solution:
    def climbStairs(self, n: int) -> int:
        # Brute Force
        # climbStairs(n) == (climbStairs(n-2) + 1(2 step action)) + (climbStairs(n-1) + 1(1 step action))
        # if n == 0 or n == 1:
            # return 1
        # else:
            # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # Dynamic Programming
        result = {0:1, 1:1}
        for n in range(2, n+1):
            result[n] = result[n-1] + result[n-2]
        return result[n]
