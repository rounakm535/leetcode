import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = []
        
        # Initialize the heap with the first k elements
        for num in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, num)
            else:
                heapq.heappushpop(self.heap, num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        
        return self.heap[0]
