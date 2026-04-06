class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two Pointer
        l, r = 0, len(numbers) - 1

        # l and r can't be the same as one element can't be used twice
        while l < r:
            cur_sum = numbers[l] + numbers[r]
            if cur_sum > target:
                r -= 1
            elif cur_sum < target:
                l += 1
            else:
                return [l+1, r+1]
