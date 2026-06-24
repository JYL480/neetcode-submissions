"""
0. First intuition
- Is that we have to find the starting thing item, 
only then we can populate the  list to get the length

- Also have a hashmap for this as well 
- or hashset to make things unqiue yeah



1. What do they want, they want you to return the length of the longest consecutive list you can get with an increment of 1 for eahch element
- Have to be done in O(N)


skip


4. Hmmm 
Will use a hash set for this, because we want to have unqiue elements???/
- Then we will find which is teh starting eleme ts in right
the create the hash set???????

- Okay it will be too complicated, but my method works oso


"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen_set = set(nums)
        # print(seen_set)
        longest = 0


        for num in seen_set:

            if num - 1 not in seen_set:
                
                length = 1
                # Then num is the start of that set

                while num + length in seen_set:
                    length+=1

                longest = max(longest, length)
            
        return longest
            
            # Okay then we have to check whehter there this is the start of the nymber if it is ee that good log

