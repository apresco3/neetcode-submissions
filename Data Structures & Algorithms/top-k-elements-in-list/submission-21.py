class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        num_count = Counter(nums)
        heapq.heapify(heap)

        for num, count in num_count.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [values for (count, values) in heap]