class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurance = {}
        for num in nums:
            if num not in occurance:
                occurance[num] = 1
            else:
                return True
        return False
