class Solution:
    def rob(self, nums: List[int]) -> int:
        table = [0 for _ in range(len(nums))]
        # Base case
        # Nums length is at least 1
        table[0] = nums[0]
        if len(nums) >= 2:
            table[1] = max(nums[1], nums[0])

        # Recurrence 
        for i in range(2, len(nums)):
            table[i] = max(table[i-2]+nums[i], table[i-1])
        
        print(table)
        return table[-1]