"""
0. Lets try this agian, yah you should be able to do this!!!

- Using nested for loops with a converging pointer

- also note that converging pointer mist of the timme you need to sort 

- should be gucci


"""



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums = sorted(nums)

        res = []

        n = len(nums)

        for i in range(n-3): # Here we are doing n-3. ,because we got 3 other things we need

            # Then deal with duplicate if the first one isnt confirmed
            if i >0 and nums[i-1] == nums[i]:
                continue

            for j in range(i + 1, n -2): # Same concept we haev to start one after, and leave 2 more behind
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

            
                l = j + 1
                r = n - 1
                
                while l <r :
                    t_sum = nums[i] + nums[j] + nums[l] + nums[r]

                    if t_sum == target:
                        res.append([nums[i] ,nums[j] ,nums[l] , nums[r]])
                        # Then here we need to move the L to prevent the 2 and 3rd to be the same 
                        while l < r and nums[l] == nums[l+1]: # So if the this l and the next l is the same move l up 
                            l += 1
                        
                        l += 1
                        r -=1 # We do this both that previous combi aldy used and we will move the ponters
                    elif t_sum < target: # Means wea re too small, we will move the L up 
                        l +=1

                    else:
                        r -=1
        return res
                    









