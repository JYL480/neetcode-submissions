"""
0. 4sum question, maybe you would need, ,nested for loop for the first 2,then have l and r pointers for the last 2
- we would need to sortye this, likely will be )n^3)



4. THis will be done in the samem concept as well yah

- NAyways you will ahave to for loops and uhh yah


- Thiis is speical question yah
- Yu need to know how to handle the duplicates within yah 
- You will also need to sort the num 


- This is a 2 pointer question, buit you have nested for loop outside for the first thingy 2 tihngy


"""



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)

        res = []
        n = len(nums)

        for i in range(n-3): # We will - because we need 3 thiings left mahh
            # Now we will deal with the duplicate

            if i>0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n-2): # we will start one afeter the prev one
                # Here also need to check the duplciate here as well
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = n - 1

                while l < r:

                    t_sum = nums[i] + nums[j] + nums[l] + nums[r]

                    if t_sum == target: # Then you will apend 
                        res.append([nums[i] , nums[j] , nums[l] , nums[r]])
                        # Then you will have to deal with duplciages again, cause 1 -1 -1 Because the L and 2nd might be the same 
                        while l < r and nums[l] == nums[l+1]:
                            l += 1

                        l += 1
                        r -= 1 # THis because we know this combi is used, thus we will move on 

                    elif t_sum > target: # Meaning that we are 2 big, we have to move down, r - = 1
                        r -=1
                    elif t_sum < target:
                        l += 1

        return res 

