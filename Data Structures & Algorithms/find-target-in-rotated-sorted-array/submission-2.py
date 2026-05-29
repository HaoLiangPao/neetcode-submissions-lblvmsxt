class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:   # left half is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1        # target is in the sorted left half
                else:
                    l = mid + 1        # target must be in the right half

            else:                      # right half is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1        # target is in the sorted right half
                else:
                    r = mid - 1        # target must be in the left half

        print(l, r)
        return -1 if (l == len(nums) or nums[l] != target) else l