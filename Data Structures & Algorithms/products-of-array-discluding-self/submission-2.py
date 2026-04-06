class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix and Suffix
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        results = [1] * len(nums)

        for i in range(0, len(nums)):
            if i-1 < 0:
                prefix[i] = 1
            else:
                prefix[i] = prefix[i-1] * nums[i-1]
        # print(f"prefix is {prefix}")
        
        for i in range(-1, -len(nums)-1, -1):
            if i+1 == 0:
                suffix[i] = 1
            else:
                suffix[i] = suffix[i+1] * nums [i+1]
            results[i] = prefix[i] * suffix[i]
            # print(f"suffix is {suffix}")
            # print(f"results is {results}")
        return results
