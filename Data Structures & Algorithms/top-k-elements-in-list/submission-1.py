from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # python only has min heap 
        heap = []
        counter = Counter(nums)
        for c in counter:
            heapq.heappush(heap, (-counter[c], -c))

        result = []
        for i in range(k):
            _, value = heapq.heappop(heap)
            result.append(-value)
        return result

