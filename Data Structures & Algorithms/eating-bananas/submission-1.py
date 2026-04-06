class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = (l + r) // 2

            # Check if mid is applicable
            hours = 0
            for p in piles:
                if p <= mid:
                    hours += 1
                else:
                    hours += math.ceil(p / mid)
            
            if hours > h:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1
        
        return res
