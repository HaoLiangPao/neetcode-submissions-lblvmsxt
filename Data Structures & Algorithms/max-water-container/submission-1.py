class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two Pointers
        result = 0 # when there is no element, the result can't be negative
        l, r = 0, len(heights) - 1
        max_l, max_r = -1, -1

        while l < r:
            # When the heights on any side increased, record it
            if heights[l] > max_l:
                max_l = heights[l]
            
            if heights[l] > max_l:
                max_l = heights[l]
            
            # Compare the maximum area
            cur_max = min(heights[l], heights[r]) * (r-l)
            if cur_max > result:
                result = cur_max
            
            # Update the shorter side among l, r
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            # When they are the same, by default change the left side
            else:
                l += 1
        return result

