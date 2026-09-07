class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 1D Dynamic Programming, from a previous target state not previous nums[:i]
        T = [0 for _ in range(target+1)]

        # Base Case:
        T[0] = 1

        # Recurrence:
        for i in range(1, target+1):
            for num in nums:
                if num <= i:
                    T[i] += T[i-num]
        return T[target]