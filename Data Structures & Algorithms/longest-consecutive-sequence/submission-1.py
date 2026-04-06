class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute force
        store = set(nums)
        res = 0

        for index, num in enumerate(nums):
            strike = 0
            # Check if it is the start of a sequence
            if num - 1 not in store:
                next_consecutive = num
                while next_consecutive in store:
                    strike += 1
                    res = max(strike, res)
                    next_consecutive += 1
        
        return res
            
