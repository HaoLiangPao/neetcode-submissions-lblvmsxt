class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Subarray, continuous
        
        # T(i) max product of the subarray within n1,n2,n3... ni which includes ni
        max_table = [-11 for _ in range(len(nums))]
        min_table = [11 for _ in range(len(nums))]

        # Base Case
        max_table[0] = nums[0] # as nums is at least 1 in length
        min_table[0] = nums[0]

        # Recurrence
        for i in range(1, len(nums)):
            # T(i) = MAX(T(i-1) * ni, ni)
            max_table[i] = max(max_table[i-1] * nums[i], min_table[i-1] * nums[i], nums[i])
            min_table[i] = min(min_table[i-1] * nums[i], max_table[i-1] * nums[i], nums[i])

        print(max_table)
        print(min_table)
        
        return max(max_table)

