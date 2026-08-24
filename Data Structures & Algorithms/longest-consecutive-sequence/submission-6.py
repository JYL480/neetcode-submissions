"""
0. When i see consecutive, or cntiguous might be a sliding windo yah 
- Urm, have to do this in a singel pass?
- Urmm, i there is no sub leh
- Nothing contiguous about this
- 2 poinnters?
- Seems like maybe use a 2 pointer for this?
- IDK

- Use a set() idk



1. THen want to return a integer

Find the the len of the a res = [] then can form a monotoic increasing thingy 

2. edge ccases?

3. Naive?
- Well you will do a nest for loop ig but you would have to rack?


4. How do you find the start of the sequence?
- for the min of set()

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)
        # We need to find what is the start of this shit fml
        longest = 0
        
        for num in nums:
            if (num-1) not in seen: # this is the start of the sequence, then we will 
                start = num - 1
                length = 0
                while (num + length) in seen:
                    length += 1
                
                longest = max(longest, length)

        return longest
                            



                