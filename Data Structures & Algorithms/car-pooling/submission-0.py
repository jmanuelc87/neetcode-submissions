class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        heap = []
        current = 0

        for passengers, start, end in trips:
            while heap and heap[0][0] <= start:
                _, out_passengers = heapq.heappop(heap)
                current -= out_passengers

            current += passengers
            if current > capacity:
                return False
            
            heapq.heappush(heap, [end, passengers])
        
        return True