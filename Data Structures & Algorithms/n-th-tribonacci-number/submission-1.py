class Solution:
    def tribonacci(self, n: int) -> int:
        # Dynamic Programming
        T = [0 for _ in range(n+1)]

        # Base Case:
        if n <= 1:
            return n
        
        T[0] = 0
        T[1] = 1
        T[2] = 1

        # Recurrence:
        for i in range(3, n+1):
            T[i] = T[i-3] + T[i-2] + T[i-1]

        return T[n]