class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Counter
        count_map = {}
        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)
        
        # Bucket Sort
        buckets = [[] for i in range(len(nums)+1)]
        for num in count_map.keys():
            count = count_map[num]
            buckets[count].append(num)
        
        # Get top k
        results = []
        for i in range (len(nums), 0, -1):
            for num in buckets[i]:
                results.append(num)
                if len(results) == k:
                    return results
