class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search as it is an ordered list
        l, r = 0, len(nums) - 1

        while l < r:
            mid = int((l + r) / 2)
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1 if nums[l] != target else l

