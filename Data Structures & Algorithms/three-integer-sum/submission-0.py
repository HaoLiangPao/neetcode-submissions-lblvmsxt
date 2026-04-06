class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force
        target = 0
        result_set = set()

        for i in range(len(nums)-2):
            n = nums[i]
            # print(f"i is {i}, n is {n}")
            two_sum = target - n
            # print(f"two_sum is {two_sum}")

            for i_2 in range(i+1, len(nums)-1):
                n_2 = nums[i_2]

                # print(f"i_2 is {i_2}, n_2 is {n_2}")
                remaining = two_sum - n_2
                # print(f"remaining is {remaining}")

                for i_3 in range(i_2+1, len(nums)):
                    n_3 = nums[i_3]

                    # print(f"i_3 is {i_3}, n_3 is {n_3}")
                    if n_3 == remaining:
                        pair = sorted([n, n_2, n_3])
                        result_set.add(tuple(pair))
        
        result = []
        for pair in result_set:
            result.append(list(pair))
        return result