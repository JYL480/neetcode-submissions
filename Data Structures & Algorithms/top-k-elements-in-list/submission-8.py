"""
0. When you see top K, you should think of using a heapq aldy. .
- This is by default, note that with a min heap
- What is the binary tree stryctyre like....
- Note that using inbuilt will be good yah 
- like with heapq, topk larget etc......

1. What do they want?
- They want to return the A list of  the top k frequenet numbers. 



4. urmmmm i dont know 



"""
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_list = {}

        for num in nums:
            hash_list[num] = 1 + hash_list.get(num, 0)

        tup_list = []
        # Then like we can convert them insto a list, heapq works with a list yah
        for l,v in hash_list.items():
            tup_list.append((v,l))
    

        top_k = heapq.nlargest(k, tup_list)

        res = []

        for i in range(k):
            
            res.append(top_k[i][1])
            
        return res
        








    
    





        