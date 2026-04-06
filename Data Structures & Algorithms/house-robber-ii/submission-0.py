class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge Case:
        if len(nums) == 1:
            return nums[0]
        # To differenciate the cicule, we can do nums[1:] and nums[:-1]
        return max(self.dp(nums[1:]), self.dp(nums[:-1]))


    def dp(self, nums: List[int]) -> int:
        # Base Cases
        rob1, rob2 = 0, 0 # rob1 is i-2 and rob2 is i-1 
        # Recurrence
        for n in nums:
            newRob = max(rob1 + n, rob2) # newRob is i
            rob1 = rob2
            rob2 = newRob
        return rob2

