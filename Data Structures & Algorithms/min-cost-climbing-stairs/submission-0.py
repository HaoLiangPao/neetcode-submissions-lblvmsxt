class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Min Cost at N = (Min Cost at N-1 + 1 step) or (Min Cost at N-2 + 1 step)
        # Target is:
        #   - position = 0 or 1
        #   - push the position to len(cost) + 1

        map = {0: 0, 1: 0}
        for index in range(2, len(cost) + 1):
            local_min_cost = min(map[index-1] + cost[index-1], map[index-2] + cost[index-2])
            map[index] = local_min_cost
        return min(map[len(cost)-1] + cost[-1], map[len(cost)-2] + cost[-2])
            