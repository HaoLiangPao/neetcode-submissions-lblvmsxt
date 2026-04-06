class Solution:
    def findMin(self, nums: List[int]) -> int:
        # We need to find the original first index which is always the minimum
        # Divide and conquer: as we know the array can always be split into two sorted array, if we find the right pivot (first or last index)
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            
            elif nums[mid] <= nums[l]:
                r = mid
            
            # If the subarray is already sorted, just return the most left element
            elif nums[l] <= nums[mid] and nums[mid] <= nums[r]:
                return nums[l]
            
            # print(f"l and r are: {l} {r}")
            
        return nums[r]

