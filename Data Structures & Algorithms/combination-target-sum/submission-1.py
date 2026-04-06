class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Multiple times usage - N % a(3) = b(4), then it can be sumed by combination of 3 and 4
        # a, b shall be the element in the nums

        # Base Case: S(0) = 0
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        # save each sum into the element set, 
            # and in the value, save the combination
        # if find another value added, add that to each combination in the value

        total = 0
        for i in range(len(nums)):
            # Check every new num with existing combinations
            for j in range(len(dp)):
                sub_total = j + nums[i]
                # print(f"sub_total is {sub_total}")
                if sub_total <= target:
                    # Inherite the combination from dp[j] and add the num to all of them
                    # print(f"dp[j] is {dp[j]}")
                    for k in range(len(dp[j])):
                        new_combo = dp[j][k] + [nums[i]]
                        dp[sub_total].append(new_combo)
        return dp[target]
                        