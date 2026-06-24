"""
0. Imemdiately when you top k frequent, then you will use a prioity list or the use of heapify yah 

1. What they wan t ?
- They want a list whcih containes the top k most frequent elements 
- Top k yeah

skip

4. You will hahve to use heap for this shit 
- to heapiify or when using heapq, it sisenlt will be a logk * n to look through all theh thingy

- Heapiigy the indices and then with the elements yeah. 
How woydl you do that
- You can populate a hash table fo rhtis?/



"""
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        res = []

        for num in nums:
            hash_table[num] = 1 + hash_table.get(num,0)

        # Then you will put them in a tuplle to solve this shit, so that you van compare with the nlargest funciton 
        for key, v in hash_table.items():
            res.append((v, key))

        top_k = heapq.nlargest(k,res)
        

        return [ tup[1] for tup in top_k]









    
    





        