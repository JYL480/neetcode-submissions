
"""
0.ofc based on the intuition this will be a heap question yah 

complexity?
- O(N)
- O(N) as well when we heapify this list of thingy
- Oh not the value
- You now what toa yi will try to memorise the

- we will do thsi heap question ah 
- The difffetence with this is that if we want to ahavve top k wiwe will be using the min heap
- Beacause we when pop the root at the top which is the min will be poppoed away which is what we want
- Somehting like that


"""

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Lets do this stupid question yah, what do they want?  
        # Go overseas loh for fun uh LOL
        min_heap = []
        count = {}
        for num in nums: 
            count[num] = 1 + count.get(num, 0)

        
        # Now thatw ew have t
        for key, count in count.items():
            heapq.heappush(min_heap, (count, key))
        
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [tu[1] for tu in min_heap]




                                