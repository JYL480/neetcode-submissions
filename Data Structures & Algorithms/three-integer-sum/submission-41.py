"""
0. This will be to find the first item them find the next, 
So it wil be a 2 pointer, with a L and R yah, it will be a converging 2 pointer for thtis yah!!


1. What does this q want?
- They want to return a list of list of teh indecies that sum ==0
- All must have distunct yah!!

2. what are teh edge cases?


3. Naive way
- Prob a nested for loop for this
- This will then become O(N^2) bad ig. Not good!!!


4. what is te olsution
for loop outside with enumerate?
So after that thef irst item, 
we have to check whether the next item is the same as the firstr
- If both same then we willl skip, bcos there will be duplicates i thik 

- Then you will have an inner for loop for this I think, which will cuase, idk we will figure it out tgt LOL

5. What are the complexities for this?/
O(N^2) ii think IDK 



"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        # FK RIGHT we have to sort
        nums = sorted(nums)
        for i in range(n-2): # We need to have 2 left for the l and r converging pointers i tihnk 
            if i>0 and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = n - 1
            while l < r: # There will be no equal yah 
                t_sum = nums[i] + nums[l] + nums[r]
                
                if t_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # Then we will try to find if there are other options within 
                    while l < r and nums[l] == nums[l +1]:
                            l +=1 
                    l += 1
                    r -=1
                
                elif t_sum > 0 :
                    r -= 1
                elif t_sum < 0:
                    l +=1 

        return res
                


            










