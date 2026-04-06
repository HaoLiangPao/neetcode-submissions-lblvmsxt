class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sorted nlogn
        nums_sorted = sorted(nums)
        print(nums_sorted)

        results = []

        # Solve a Two Sum question for each number (n^2)
        for i, n in enumerate(nums_sorted):
            if n > 0:
                break
            if i > 0 and n == nums_sorted[i-1]:
                continue
            two_sum = 0 - n
            # print(f"Select {n}, looking for ({two_sum})")

            l, r = i + 1, len(nums_sorted)-1
            while l < r:
                # print(f"Left is {l}, right is {r}")
                # Current selection is larger than two_sum, move right pointer
                cur_sum = nums_sorted[l] + nums_sorted[r]
                if cur_sum > two_sum:
                    r -= 1
                # Current selection is smaller than two_sum, move left pointer
                elif cur_sum < two_sum:
                    l += 1
                else:
                    results.append([n, nums_sorted[l], nums_sorted[r]])
                    l += 1
                    r -= 1
                    while nums_sorted[l] == nums_sorted[l-1] and l < r:
                        l += 1
        return results
