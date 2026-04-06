class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute Force O(n^2)
        results = []
        for i, n in enumerate(nums):
            product = 1
            for other_n in nums[0:i]:
                product *= other_n
            for other_n in nums[i+1:]:
                product *= other_n
            results.append(product)
        return results