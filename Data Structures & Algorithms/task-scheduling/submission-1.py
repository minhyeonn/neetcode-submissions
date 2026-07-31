class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}

        for letter in tasks:
            count[letter] = count.get(letter, 0) + 1
        
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)


        res = 0
        cooldown = deque()
    
        while max_heap or cooldown:
            res+=1

            if max_heap:
                count = heapq.heappop(max_heap) + 1
                if count != 0:
                    cooldown.append((count, res + n))
            

            if cooldown and cooldown[0][1]==res:
                heapq.heappush(max_heap, cooldown.popleft()[0])
        return res
  