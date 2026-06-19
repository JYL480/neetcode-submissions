"""
0. When they want top k frequenet elements, you will think immeidate of heap or prorioty queue yah


1. What they want?

- Return the values of the top k kelements. It can be in any order. 
- Return a list
- 

4. pattern?
- I will use a counter dict, ,then use a tuple to contain in the heap 
- which will then I wil luse the klargest to compare the first item inn the tuple 
O(nlogk)
- 


"""

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict = {}
        
        for num in nums:
            counter_dict[num] = 1 + counter_dict.get(num, 0)


        # I will do a tuple thingy in a list

        tup_list = []

        for key,count in counter_dict.items():
            tup_list.append((count, key))
        
        top_k = heapq.nlargest(k, tup_list)
        
        print(top_k)

        res = []
        for tup in top_k:
            res.append(tup[1])
        print(res)
        
        return res
    
    





        