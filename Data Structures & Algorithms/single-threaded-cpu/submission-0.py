class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available = []
        pending = []

        for i, (enqueueTime, processingTime) in enumerate(tasks):
            heapq.heappush(pending, (enqueueTime, processingTime, i))

        res = []
        time = 0
        while available or pending:
            while pending and pending[0][0] <= time:
                enqueueTime, processingTime, i = heapq.heappop(pending)
                heapq.heappush(available, (processingTime, i))

            if not available:
                time += pending[0][0]
                continue
            
            processingTime, i = heapq.heappop(available)
            time += processingTime
            res.append(i)

        return res