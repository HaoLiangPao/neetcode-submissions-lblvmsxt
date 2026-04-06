class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        # print(N)


        if sum(nums) % 2 != 0:
            return False
        # Then we just need to find the set that nums up to target, as the rest will sum up to target automatically
        target = sum(nums) // 2
        # print(target)

        table = [[False for _ in range(target+1)] for _ in range(N)]


        # Base cases
        for i in range(N):
            table[i][0] = True          # sum 0 always possible
        if nums[0] <= target:
            table[0][nums[0]] = True    # first element alone

        # Recurrence
        for i in range(1, N):           # start from 1, not 0
            for j in range(1, target + 1):
                if j < nums[i]:         # can't include nums[i]
                    table[i][j] = table[i-1][j]
                else:                   # exclude OR include
                    table[i][j] = table[i-1][j] or table[i-1][j - nums[i]]
        # print(table)

        return table[N-1][target]

        