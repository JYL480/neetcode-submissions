"""
0. Wlets try htis 3 sum problem again yah!!

1. What is the intuition for htis!
- You will have a 2 pointer converging left and right 
- You will also have to check for duplicates yah! THis is very implpoprtant!!
- Note that how this 2 poinnter converging works with nums is that we have to sort everythign out yah !!
- It has to be sorted hor!!!! 
- THis is very important!

4. Lets skip to the 4th one yah 



"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums = sorted(nums)

        for i in range(n - 2): # Here we will have to -2 because we are doing the we need to leave the l and r behind yah 
            if i > 0 and nums[i] == nums[i-1]: # Makes sense to be - 1 because we are doing after the first
                continue

            l = i + 1
            r = n - 1

            while l < r:
                t_sum = nums[i]  + nums[l] + nums[r]

                if t_sum == 0:
                    # Meaning that we will append then find out if there are l and r pairs
                    res.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l+1]:
                        l +=1

                    # else you will move both l and r because this pair will be used
                    l += 1
                    r -=1

                elif t_sum < 0: # Hence the sorted yah, this works because of that!
                    l +=1 
                elif t_sum > 0:
                    r -=1

        return res
    










