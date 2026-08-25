"""
0. do this question again plz!!1
- What do they wantn?
- This is one is quite simple, if you draw it out on a number line yah 


- So which one?????????

4. Create a set, and check which one is the start of the thingy yah 
- Then you will count the number of consecutive thingys there are inside the thingy 



"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)


        longest = 0

        for num in nums:
            # check if its the first of the seuqenece 
            if (num - 1) not in seen:
                # Meaning num is the start
                leng = 0 

                while (num + leng) in seen:
                    leng += 1
                longest = max(longest, leng)

            else: 
                continue
        return longest 

                