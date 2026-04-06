class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        
        # Base Case: T(0) = 1 (each num is a increasing subsequence by itself)
        table = [1 for _ in range(N)]

        # Recurrence
        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    table[i] = max(table[i], table[j] + 1)
        
        print(table)

        return max(table)

