"""
0. Immediate intuituiion?
- When I see top k, you will go with a priority queue or a min heap / max heap ts

1. Rephrase?
    - Return the a list of the most frequent elements top k. 
    - Not index but the actual elements inside
    - Answer will always be unique yah

2. Edge cases?
    - When ehtere are only the same numbers, then it will only be that one.

3. Naive? 
    - Have some dict to count

4. Pattern, I will use a tuple heap to compare!!


5. complexity?
    - To heapify, it will take O(N), because we look at alll the numbers
    - Anythin else will be to logn yyah
    - Then can use nlargest(k, list), which is O(Nlogk), K because we are only looking at uptill that node in teh binary tree




"""

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We will do a counter first yah 
        counter_num = {}

        for num in nums:
            counter_num[num] = 1 + counter_num.get(num, 0)
        
        # After doing the counter, I will want to heapify ts by placing list of tuples. Their corresponding number 
        # And the the counter, When compariing nlargest ir wut ggeaout wukk cinoare wutg tge furst ioeratibb giw 
        # [(1,1),(2,2)....]
        list_num = []
        for key,v in counter_num.items():
            list_num.append((v,key))
        
        # I will now heapify this 

        heapq.heapify(list_num)

        # Use the heapq top k function yab \
        k_largest = heapq.nlargest(k, list_num)
        print(k_largest)
        res = []
        for tup in k_largest:
            res.append(tup[1])
        print(res)

        return res
        







        