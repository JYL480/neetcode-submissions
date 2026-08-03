"""
0. Intuition
- hMMMMMMMM
- I want to think converging pointer for this????
- 1 at the front and end
- I believe we will have another pointner?
- Intuition will be to sort?
- When you sort it will be onlogn
- I would think to sort this shit first 

- We will sort frst, then have l and r, and at the same time a for loop
- Have to see the first if the first 2 are the same, last will be the same 



"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums = sorted(nums)



        for i, num in enumerate(nums):

            # Hmm make sense for the l and r to be dynamic right    
            l = i + 1 
            r = len(nums) - 1
            
            #  Her you will do the cheking 
            # What do you mean?
            # If the first one and the next is the same
            if i > 0 and nums[i -1] == num:
                # meaning it will be the same rght
                continue

            while l < r:

                
                t_sum = nums[l] + nums[r] + num
                
                # I have to heck for dupllicates yah cause they want it to be dinstnct 
                if t_sum < 0: # Meaning we can move up yah
                    l += 1
                elif t_sum > 0: # Too bug, r move down
                    r -= 1
                elif t_sum == 0 :

                    res.append([nums[l], nums[r], num]) # Right because no return, ti will styck 
                    
                    l += 1
                    # urm then nyou can habe nothe while loop sinisde right
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res



















        