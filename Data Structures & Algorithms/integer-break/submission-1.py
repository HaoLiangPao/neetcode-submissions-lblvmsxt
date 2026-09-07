class Solution:
    def integerBreak(self, n: int) -> int:
        # Base Case: T[0] = 1, T[1] = 1, T[2] = 1
        T = [i for i in range(n+1)]
        T[0] = 1

        if n == 2:
            return 1
        if n == 3:
            return 2

        for i in range(1, n+1):
            for j in range(1, i):
                T[i] = max(T[i], T[i-j] * T[j])
        
        return T[n]