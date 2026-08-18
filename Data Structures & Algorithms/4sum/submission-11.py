"""
0. 4sum question, maybe you would need, ,nested for loop for the first 2,then have l and r pointers for the last 2
- we would need to sortye this, likely will be )n^3)



4. So will have 2 for loop fir 
then a while loop for the 3ed i guess

"""



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []   
        nums = sorted(nums)

        n = len(nums)

        for i in range(n-3):
            # Then you will do you duplicate here
            if i >0 and nums[i] == nums[i-1]:
                continue    
            
            for j in range(i + 1, n - 2): 

                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = n - 1

                while l<r:
                    t_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    if t_sum == target :
                        res.append([nums[i], nums[j], nums[l], nums[r]])

                        while l <r and nums[l] == nums[l+1]:
                            l +=1
                        l +=1 
                        r -=1
                    elif t_sum > target:
                        r -= 1
                    else:
                        l += 1
        return res






