"""
1. return the top k most frequent number in the list
    - return a list and the actual unique numbers are inside. 
    - It can be returned in any order yah

2. Edge?
    - When THere is only 1 nymber?
        - Then return that only nuymber
    - duplicate nymber
        - Will that unique number
    
3. Naive solution?
    - My first instinct to use a hash map?
    - with a seen dict which will count, then return the the top 2. LOL

    - Is this a naive idk....

4. What will be time and space 
    - I guess we are using heap hor, when doing top k yah. This is important to note hor!!!
    - Then it will be log nlog ish i think. 



"""

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter_dict = {}
        for num in nums:
            counter_dict[num] = 1 + counter_dict.get(num, 0)
        print(counter_dict)

        count_list = list(counter_dict.values())
        
        tup_list = []
        for j, v in counter_dict.items():
            tup_list.append((v,j))
        
        heapq.heapify(tup_list)
        print("d",tup_list)
        k_largest = heapq.nlargest(k, tup_list)
        print(k_largest) # Wait no this is the key number yah then i will get
        re_list = []
        for v in k_largest:
            print(v)
            re_list.append(v[1])
        print(re_list)
        return re_list





        