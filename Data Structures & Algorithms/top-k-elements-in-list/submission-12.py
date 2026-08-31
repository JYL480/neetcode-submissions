
"""
0.ofc based on the intuition this will be a heap question yah 

complexity?
- O(N)
- O(N) as well when we heapify this list of thingy
- Oh not the value


"""


import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap =  []
        hs = {}
        for num in nums:
            hs[num] = 1 + hs.get(num, 0)


        for c,v in hs.items():
            heapq.heappush(max_heap, (v, c))

            #onlu will be done once if im not wrong# If there is more thatn the size pop out this is a logN time yah
            if len(max_heap)>k:
                heapq.heappop(max_heap)


        print(max_heap)

        return [tu[1] for tu in max_heap]

