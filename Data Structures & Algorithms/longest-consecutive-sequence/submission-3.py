"""
0. Intuition?
- Created seen hashmap, with a set. 
- Check if there is a plus 1 value in the set. 
- if so then return ....

1. What they want?
- Return the len of the consecutive sequence that is +1 from each other
- Do it in o(n) time

2. edge cases?
- Where there is nothing, then return 0 

3. Naive?
    - Im not really sure leh

3. Pattern?
    - Will create a seen hash set()
    - Then Will see if tehre is a plus 1
    - with a counter

4. Complexity 
time = O(N)
spac will be O(N)


"""
from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_list = defaultdict(list)
        # Inside will contain the starting and then the chain of numbers
        seen_num = set(nums)
        longest = 0
        starting_no = 0

        for num in nums:
            if num - 1 not in seen_num: # That means this is a start of the sequence
                starting_no = num - 1
                hash_list[num]

        # print(hash_list)
        # Now to populate inside bah
        for k in hash_list.keys():
            key = k
            while key in seen_num: 
                hash_list[k].append(key)
                key+=1
                # print(key)

            


        for value_list in hash_list.values():
            if len(value_list) > longest:
                longest = len(value_list)
        
        return longest


