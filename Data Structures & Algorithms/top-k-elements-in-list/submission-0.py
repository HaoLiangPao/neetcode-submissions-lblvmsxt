class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Counter
        count_map = {}
        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)

        # K-size heap
        my_heap = []
        for num in count_map.keys():
            heapq.heappush(my_heap, (count_map[num], num))
            if len(my_heap) > k:
                heapq.heappop(my_heap)
        
        # Get top k occurance number
        result = []
        for i in range(k):
            result.append(heapq.heappop(my_heap)[1])
        return result

        