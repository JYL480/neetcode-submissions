"""
0. 4sum question, maybe you would need, ,nested for loop for the first 2,then have l and r pointers for the last 2
- we would need to sortye this, likely will be )n^3)



4. THis will be done in the samem concept as well yah

- NAyways you will ahave to for loops and uhh yah

"""



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        n = len(nums)
        
        for i in range(n - 3): # why 3 because we need the next and then l and r yah 
            # Checl for the first and next duplicates
            if i >0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i + 1, n -2): # I thinkg this is the nerxt few yah  whihc is n-2 because l and r and i +1 is the the one after
                if j > i +1 and nums[j] == nums[j-1]:
                    continue
                
                l = j + 1
                r = n - 1

                while l<r:
                    t_sum = nums[i] + nums[j] + nums[l] + nums[r]

                    if t_sum == target:
                        res.append([nums[i] ,  nums[j] ,  nums[l], nums[r]])

                        while l <r and nums[l] == nums[l + 1]:
                            l += 1
                        l += 1
                        r -= 1
                    elif t_sum > target:
                        r -=1
                    else:
                        l += 1
        return res

