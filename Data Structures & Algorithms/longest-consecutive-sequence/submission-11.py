"""
solve again loh

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        longest = 0

        for num in nums:
            
            # try to alwasy process first
            if (num - 1) not in seen:
                 # this is the start of this shit
                # Start is the start of the sequence 
                leng = 1
            
                while (num + leng) in seen:
                    leng += 1
                longest = max(longest, leng)
            
        return longest
    



                